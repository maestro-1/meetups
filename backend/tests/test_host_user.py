import json
import unittest
from base import BaseTestCase


class HostTest(BaseTestCase):
    """docstring for HostTest"""

    def test_get_profile(self):
        with self.client:
            headers = {}
            log_in = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )

            token = json.loads(log_in.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            response = self.client.get(
                '/profile/2',
                headers=headers
            )
            check = json.loads(response.data.decode('utf-8'))['full_name']

            self.assertEqual(response.status_code, 200)
            self.assertIn('Osakwe Chuwkuka', check)

    def test_update_profile(self):
        with self.client:
            headers = {}
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )
            # print((response.data.decode('utf-8')))
            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            response = self.client.put(
                '/profile/1',
                headers=headers,
                content_type='application/json',
                data=json.dumps({'full_name': 'akachuwku aniakor',
                                 'contact': '090549812758', 'email': 'anino@gmail.com'})
            )

    def test_delete_account(self):
        with self.client:
            headers = {}
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )
            # print((response.data.decode('utf-8')))
            token = json.loads(response.data.decode('utf-8'))['token']
            headers['Authorization'] = 'Bearer {}'.format(token)

            response = self.client.delete(
                '/profile/1',
                headers=headers
            )
            # print(response.data)
            self.assertEqual(response.status_code, 203)
            self.assertIn('account deleted',
                          json.loads(
                              response.data.decode('utf-8'))['msg']
                          )

    def test_401_for_profile_route(self):
        with self.client:
            get_response = self.client.get(
                '/profile/1',
            )
            self.assert401(get_response)
            error = json.loads(get_response.data.decode('utf-8'))

            self.assertEqual('Missing Authorization Header',
                             error['msg'])

    def test_403_for_profile_delete(self):
        with self.client:
            headers = {}
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )

            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            response = self.client.delete(
                '/profile/2',
                headers=headers
            )
            self.assert403(response)

    def test_403_for_profile_update(self):
        with self.client:
            headers = {}
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )

            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            response = self.client.put(
                '/profile/2',
                headers=headers,
                content_type='application/json',
                data=json.dumps({'email': 'akachuku@gmail.com'})
            )
            self.assertEqual(response.status_code, 403)

    def test_404_for_user_profile(self):
        with self.client:
            headers = {}
            log_in = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )

            token = json.loads(log_in.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            response = self.client.get(
                '/profile/12',
                headers=headers
            )
            self.assert404(response)


if __name__ == '__main__':
    unittest.main()
