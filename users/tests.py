from django.urls import reverse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

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
            'category': 'SALES',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_create_user_wrong_confirm_password(self):
        url = reverse('register')
        data = {
            'username': 'spy',
            'first_name': 'james',
            'last_name': 'bond',
            'email': 'jb@email.com',
            'password': '007',
            'confirm_password': '008',
            'category': 'SALES',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)
        self.assertRaises(ValidationError)

    def test_login(self):
        CustomUser.objects.create_user(username='test', password='1234')
        response = self.client.login(username='test', password='1234')
        self.assertTrue(response)


    def test_logout(self):
        url = reverse("logout")
        user = CustomUser.objects.create_user(username='test', password='1234')
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
