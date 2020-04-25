import json
import unittest
from base import BaseTestCase


class GuestTest(BaseTestCase):
    """docstring for GuestTest"""

    def test_register_for_event(self):
        with self.client:
            response = self.client.post(
                '/meetup/1/register',
                content_type='application/json',
                data=json.dumps({'full_name': 'precious umeh',
                                 'contact': '090549812758', 'email': 'jose@gmail.com'})
            )
            self.assertEqual(response.status_code, 201)
            self.assertIn(b'Registration complete', response.data)

    def test_bad_requet_key_error_registration_for_event(self):
        with self.client:
            response = self.client.post(
                '/meetup/1/register',
                content_type='application/json',
                data=json.dumps({'full': 'Jane Doe',
                                 'contact': '090549812758', 'email': 'jose@gmail.com'})
            )
            self.assert400(response)

    def test_validation_error__for_register_for_event(self):
        with self.client:
            response = self.client.post(
                '/meetup/1/register',
                content_type='application/json',
                data=json.dumps({'full_name': 'Dorcas banner',
                                 'contact': '090549812758', 'email': 'jose@gmail'})
            )
            self.assert400(response)

    def test_unregister_for_event(self):
        with self.client:
            response = self.client.post(
                '/meetup/1/unregister',
                content_type='application/json',
                data=json.dumps({'full_name': 'David Benz',
                                 'contact': '07021954837', 'email': 'Benz@gmail.com'})
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You have been unregistered for this event', response.data)

    def test_unregister_for_event_when_not_registered(self):
        with self.client:
            response = self.client.post(
                '/meetup/1/unregister',
                content_type='application/json',
                data=json.dumps({'full_name': 'evidence daniels',
                                 'contact': '090549812758', 'email': 'joey@gmail.com'})
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'you are not registered', response.data)


if __name__ == '__main__':
    unittest.main()
