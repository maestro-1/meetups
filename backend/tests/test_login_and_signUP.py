import json
import unittest
from base import BaseTestCase


class Login(BaseTestCase):
    """docstring for Login"""

    def test_correct_login(self):
        response = self.client.post(
            '/login',
            content_type='application/json',
            data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
        )
        user = json.loads(response.data.decode('utf-8'))

        self.assert200(response)
        self.assertEqual('chuwk32@gmail.com', user['user']['email'])

    def test_faulty_login(self):
        response = self.client.post(
            '/login',
            content_type='application/json',
            data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'jimmy'})
        )
        error = json.loads(response.data.decode('utf-8'))

        self.assert400(response)
        self.assertEqual(error['msg'], 'Invalid Username or password')


class SignUp(BaseTestCase):
    """docstring for SignUp"""

    def test_proper_signUp(self):
        with self.client:
            response = self.client.post(
                '/signup',
                content_type='application/json',
                data=json.dumps({'email': 'ruon32@gmail.com',
                                 'password': '#Jimmy32', 'full_name': 'Sixtus Ruona',
                                 'contact': '0901234445'})
            )
            self.assertEqual(response.status_code, 201)
            self.assertIn(b'Welcome', response.data)

    def test_password_too_short(self):
        with self.client:
            response = self.client.post(
                '/signup',
                content_type='application/json',
                data=json.dumps({'email': 'ruon32@gmail.com',
                                 'password': '#Jane3', 'full_name': 'Sixtus Ruona',
                                 'contact': '0901234445'})
            )
            # self.assertRaises()

    # def test_password_not_strong(self):
    #     with self.client:
    #         response = self.client.post(
    #             '/signup',
    #             content_type='application/json',
    #             data=json.dumps({'email': 'ruon32@gmail.com',
    #                              'password': '#Jane3', 'full_name': 'Sixtus Ruona',
    #                              'contact': '0901234445'})
    #         )
    #         print(response)
            # self.assertRaises()

    def test_if_password_is_hashed(self):
        pass

    # def test_email_already_used(self):
    #     with self.client:
    #         response = self.client.post(
    #             '/signup',
    #             content_type='application/json',
    #             data=json.dumps({'email': 'ruon32@gmail.com',
    #                              'password': '#Jane3', 'full_name': 'Sixtus Ruona',
    #                              'contact': '0901234445'})
    #         )
        # self.assertRaises()

    # def test_Invalid_email(self):
    #     with self.client:
    #         response = self.client.post(
    #             '/signup',
    #             content_type='application/json',
    #             data=json.dumps({'email': 'ruon32@gmail.com',
    #                              'password': '#Jane3', 'full_name': 'Sixtus Ruona',
    #                              'contact': '0901234445'})
    #         )
        # self.assertRaises()


if __name__ == '__main__':
    unittest.main()
