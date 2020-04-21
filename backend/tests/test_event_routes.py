import json
import unittest
from base import BaseTestCase


class EventTest(BaseTestCase):
    """docstring for EventTest"""

    def test_get_all_events(self):
        response = self.client.get('/meetups')
        # print(response.data)
        self.assert200(response)

    def test_get_single_event(self):
        response = self.client.get('/meetup/1')
        self.assert200(response)
        # self.assertEqual(b'location: Delta, Nigeria', response.data)

    def test_404_for_unavailable_event(self):
        response = self.client.get('/meetup/25')
        self.assert404(response)
        # self.assertIn()

    def test_create_event_successfully(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
            )
            print(response.data.decode('utf-8'))
        # headers = {}
        # headers['Authorization'] = response.data['token']
        # headers['content-type'] = response.data['token']

        # file_upload_response = self.client.post(
        #     '/meeetup/create/file', buffered=True,

        #     # set authrization and multipart form headers
        #     content_type='multipart/form-data',
        #     headers=headers,

        #     data={'file': open('test.jpg', 'rb')}
        # )

        # created_response = self.client.post(
        #     '/meetups/create',
        #     data=dict(title='', description='',
        #               location='', date=''))


if __name__ == '__main__':
    unittest.main()
