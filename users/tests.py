from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CustomUser


class UserTestCase(APITestCase):

    def test_create_user(self):
        url = reverse('register')
        data = {
            'username': 'spy',
            'first_name': 'james',
            'last_name': 'bond',
            'email': 'jb@email.com',
            'password': '007',
            'confirm_password': '007',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "spy")

    def test_login(self):
        CustomUser.objects.create_user(username='test', password='1234')
        response = self.client.login(username='test', password='1234')
        self.assertTrue(response)
