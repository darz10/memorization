from django.shortcuts import reverse

from .base import BaseTestCase


class UserTestCase(BaseTestCase):
    """
    Testing for UserViewSet
    """
    def test_create_user(self):
        data = {
            "first_name": "TestUser1",
            "last_name": "testuser1",
            "email": "testuser1@gmail.com"

        }
        urlname = self.get_urlname('user-list')
        response = self.client.post(path=reverse(urlname), data=data)
        self.assertEqual(response.status_code, 201)

    def test_wrong_data_create_user(self):
        data = {
            "first_name": "Test1",
            "last_name": "test1"

        }
        urlname = self.get_urlname('user-list')
        response = self.client.post(path=reverse(urlname), data=data)
        self.assertEqual(response.status_code, 400)

    def test_authorize_user(self):
        urlname = self.get_urlname('user-authorize')
        data = {
            "email": self.user2_email,
            "password": self.password
        }
        response = self.client.post(
            path=reverse(
                urlname,
            ),
            data=data
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()["token"])

    def test_get_user(self):
        self.login(self.user2_email)
        urlname = self.get_urlname('user-detail')
        response = self.client.get(
            path=reverse(
                urlname,
                args=(self.user.id,)
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.user.id)

    def test_patch_user(self):
        self.login(self.user2_email)
        urlname = self.get_urlname('user-detail')
        new_last_name = "changed"
        data = {
            "last_name": new_last_name
        }
        response = self.client.patch(
            path=reverse(
                urlname,
                args=(self.user.id,)
            ),
            data=data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['last_name'], new_last_name)

    def test_delete_user(self):
        self.login(self.user2_email)
        urlname = self.get_urlname('user-detail')
        response = self.client.delete(
            path=reverse(
                urlname,
                args=(self.user.id,)
            ),
        )
        self.assertEqual(response.status_code, 200)
