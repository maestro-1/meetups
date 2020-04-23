import json
import unittest
from base import BaseTestCase


class EventTestSucces(BaseTestCase):
    """docstring for EventTest"""

    def test_get_all_events(self):
        response = self.client.get('/meetups')
        self.assert200(response)

    def test_get_single_event(self):
        response = self.client.get('/meetup/1')
        self.assert200(response)
        self.assertEqual('Delta, Nigeria',
                         json.loads(response.data.decode('utf-8'))['location'])

    def test_successfully_create_event_with_image(self):
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


    def test_event_update(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'chuwk32@gmail.com', 'password': 'Smaug'})
            )
            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            update_event_response = self.client.put(
                '/meetup/1/edit',
                headers=headers,
                content_type='application/json',
                data=json.dumps({'title': 'Heart Enlargemen', 'description': 'The gospel enlarging your heart',
                                 'location': 'Ibadan, Nigeria', 'date': '2020-10-12, 12:00'})
            )
            self.assert200(update_event_response)
=======


    def test_event_delete(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='application/json',
                data=json.dumps({'email': 'anino@gmail.com', 'password': 'Ariana'})
            )
            token = json.loads(response.data.decode('utf-8'))['token']
            headers = {}
            headers['Authorization'] = 'Bearer {}'.format(token)

            delete_event_response = self.client.delete(
                '/meetup/1/edit',
                headers=headers
            )
            self.assertEqual(delete_event_response.status_code, 203)
            # self.assertEqual('event deleted', json.loads(delete_event_response.data)['msg'])


if __name__ == '__main__':
    unittest.main()
