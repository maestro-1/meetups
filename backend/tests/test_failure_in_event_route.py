import json
import unittest
from base import BaseTestCase


class EventTestFail(BaseTestCase):
    """docstring for EventTest"""

    def test_404_for_unavailable_event(self):
        response = self.client.get('/meetup/25')
        self.assert404(response)

    def test_fail_create_event_with_bad_image(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
            )
            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            file_upload_response = self.client.post(
                '/meetup/create/file', buffered=True,

                # set authrization and multipart form headers
                content_type='multipart/form-data',
                headers=headers,

                data={'imageUrl': open('Nuxtjs-Cheat-Sheet.pdf', 'rb')}
            )

            headers['content-type'] = 'application/json'

            created_response = self.client.post(
                '/meetup/create',
                headers=headers,
                data=json.dumps(dict(title='Heaven Come', description='Gospel concert',
                                     location='Pennsylvania', date='2020-10-12, 10:30')))

            self.assertEqual(406, created_response.status_code)
            self.assertEqual(file_upload_response.data, b'done')
            self.assertIn('Not a valid Image',
                          json.loads(created_response.data.decode('utf-8'))['msg'])

    def test_need_to_login_for_access_route(self):

        headers = {}

        error_response_new = self.client.post(
            '/meetup/create',
            headers=headers,
            data=json.dumps(dict(title='Heaven Come', description='Gospel concert',
                                 location='Pennsylvania', date='2020-10-12, 10:30')))
        error = json.loads(error_response_new.data.decode('utf-8'))
        # print(created_response.data)
        self.assert401(error_response_new)
        self.assertEqual('Missing Authorization Header',
                         error['msg'])

    def test_403_error_in_event_update(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
            )
            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            delete_event_response = self.client.put(
                '/meetup/2/edit',
                headers=headers,
                content_type='application/json',
                data=json.dumps({'title': 'Heart Enlargemen', 'description': 'The gospel enlarging your heart',
                                 'location': 'Ibadan, Nigeria', 'date': '2020-10-12, 12:00'})
            )
            self.assert403(delete_event_response)

    def test_403_error_in_event_delete(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
            )
            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            delete_event_response = self.client.delete(
                '/meetup/2/edit',
                headers=headers
            )
            self.assert403(delete_event_response)

    def test_401_error_in_event_edit_route(self):
        with self.client:
            failed_response = self.client.delete(
                '/profile/1',
            )
            self.assert401(failed_response)


if __name__ == '__main__':
    unittest.main()
