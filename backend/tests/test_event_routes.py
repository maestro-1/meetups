import json
import unittest
from base import BaseTestCase


class EventTest(BaseTestCase):
    """docstring for EventTest"""

    def test_get_all_events(self):
        response = self.client.get('/meetups')
        self.assert200(response)

    def test_get_single_event(self):
        response = self.client.get('/meetup/1')
        self.assert200(response)
        self.assertEqual('Delta, Nigeria',
                         json.loads(response.data.decode('utf-8'))['location'])

    def test_404_for_unavailable_event(self):
        response = self.client.get('/meetup/25')
        self.assert404(response)
        self.assertIn(b'<title>404 Not Found</title>', response.data)

    def test_successfully_create_event_image(self):
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

                data={'imageUrl': open('test.jpg', 'rb')}
            )

            headers['content-type'] = 'application/json'

            created_response = self.client.post(
                '/meetup/create',
                headers=headers,
                data=json.dumps(dict(title='Heaven Come', description='Gospel concert',
                                     location='Pennsylvania', date='2020-10-12, 10:30')))

            self.assertEqual(created_response.status_code, 201)
            self.assertEqual(b'done', file_upload_response.data)
            self.assertEqual('Heaven Come',
                             json.loads(created_response.data.decode('utf-8'))['title'])

    def test_successfully_create_event_with_bad_key(self):
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

                data={'file': open('Nuxtjs-Cheat-Sheet.pdf', 'rb')}
            )

            headers['content-type'] = 'application/json'

            created_response = self.client.post(
                '/meetup/create',
                headers=headers,
                data=json.dumps(dict(title='Heaven Come', description='Gospel concert',
                                     location='Pennsylvania', date='2020-10-12, 10:30')))

            self.assertEqual(created_response.status_code, 201)
            self.assertEqual(b'default.jpg', file_upload_response.data)
            self.assertEqual('Heaven Come',
                             json.loads(created_response.data.decode('utf-8'))['title'])

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
            self.assertIn(b'Not an Image', created_response.data)

    def test_need_to_login_for_access(self):
        pass
        # with self.client:
        #     response = self.client.post(
        #         '/login',
        #         content_type='application/json',
        #         data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
        #     )
        #     token = json.loads(response.data.decode('utf-8'))['token']
        #     headers = {}
        #     headers['Authorization'] = 'Bearer {}'.format(token)

        #     file_upload_response = self.client.post(
        #         '/meetup/create/file', buffered=True,

        #         # set authrization and multipart form headers
        #         content_type='multipart/form-data',
        #         headers=headers,

        #         data={'imageUrl': open('Nuxtjs-Cheat-Sheet.pdf', 'rb')}
        #     )

        #     headers['content-type'] = 'application/json'

        #     created_response = self.client.post(
        #         '/meetup/create',
        #         headers=headers,
        #         data=json.dumps(dict(title='Heaven Come', description='Gospel concert',
        #                              location='Pennsylvania', date='2020-10-12, 10:30')))

        #     self.assertEqual(406, created_response.status_code)
        #     self.assertEqual(file_upload_response.data, b'done')
        #     self.assertIn(b'Not an Image', created_response.data)

    def test_event_update(self):
        pass

    def test_event_delete(self):
        pass


if __name__ == '__main__':
    unittest.main()
