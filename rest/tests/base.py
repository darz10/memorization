from datetime import datetime
from django.shortcuts import reverse
from rest_framework.test import APITestCase

from accounts.models import User
from reminder.models import Reminder


class BaseTestCase(APITestCase):

    auth_root_name = 'rest'

    user_email = 'test@mail.ru'
    user2_email = 'test2@mail.ru'

    password = 'password123!'

    def setUp(self):
        super().setUp()
        self.user = User.objects.get_or_create(
            first_name="test",
            last_name="testing",
            email=self.user2_email
        )[0]
        self.user.set_password(self.password)
        self.user.save()

        self.reminder = Reminder.objects.get_or_create(
            user=self.user,
            text="text default test"
        )[0]

    def login(self, phone):
        urlname = self.get_urlname('user-authorize')
        data = {'email': phone, 'password': self.password}
        response = self.client.post(path=reverse(urlname), data=data)
        token = response.json().get('token', "")
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def get_urlname(self, name):
        '''
        Получить условное название пути запроса
        '''
        return '{}:{}'.format(self.auth_root_name, name)
