from django.shortcuts import reverse

from .base import BaseTestCase


class ReminderTestCase(BaseTestCase):
    """
    Testing for ReminderViewSet
    """
    def test_create_reminder_unauthorized(self):
        data = {
            "text": "test text for reminder"
        }
        urlname = self.get_urlname('reminder-list')
        response = self.client.post(path=reverse(urlname), data=data)
        self.assertEqual(response.status_code, 401)

    def test_create_reminder(self):
        self.login(self.user2_email)
        data = {
            "text": "test text for reminder"
        }
        urlname = self.get_urlname('reminder-list')
        response = self.client.post(path=reverse(urlname), data=data)
        self.assertEqual(response.status_code, 201)

    def test_wrong_data_create_reminder(self):
        self.login(self.user2_email)
        data = {
            "textt": "Test1",
        }
        urlname = self.get_urlname('reminder-list')
        response = self.client.post(path=reverse(urlname), data=data)
        self.assertEqual(response.status_code, 400)

    def test_get_reminder(self):
        self.login(self.user2_email)
        urlname = self.get_urlname('reminder-detail')
        response = self.client.get(
            path=reverse(
                urlname,
                args=(self.reminder.id,)
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], self.reminder.id)

    def test_patch_reminder(self):
        self.login(self.user2_email)
        urlname = self.get_urlname('reminder-detail')
        new_text = "changed text"
        data = {
            "text": new_text
        }
        response = self.client.patch(
            path=reverse(
                urlname,
                args=(self.reminder.id,)
            ),
            data=data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['text'], new_text)

    def test_delete_reminder(self):
        self.login(self.user2_email)
        urlname = self.get_urlname('reminder-detail')
        response = self.client.delete(
            path=reverse(
                urlname,
                args=(self.reminder.id,)
            ),
        )
        self.assertEqual(response.status_code, 204)
