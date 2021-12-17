from datetime import time
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser

from .models import Client, Contract, Event, Status
from django.utils import timezone

class ClientTestCase(APITestCase):
    def setUp(self):
        self.client_test = Client.objects.create(
            first_name='harry',
            last_name='potter',
            email='hp@email.com',
            phone='1111',
            company='Poudlard',
        )
        self.user = CustomUser.objects.create_user(username='test', password='1234', category="SALES")
        Contract.objects.create(
            sales_contact=self.user,
            client=self.client_test,
            amount=10,
            payment_due=timezone.now()
        )

    def test_create_client(self):
        url = reverse('client-list')
        data = {
            'first_name': 'james',
            'last_name': 'bond',
            'email': 'jb@email.com',
            'phone': '1234',
            'company': 'Pikachu',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 2)

    def test_update_client(self):
        self.client.login(username='test', password="1234")
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        data = {
            'first_name': 'al',
            'last_name': 'pacino',
            'phone': '789',
            'company': 'Movie',
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Client.objects.count(), 1)
        self.client_test.refresh_from_db()
        self.assertEqual(self.client_test.first_name, "al")

    def test_delete_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.count(), 0)


class ContractTestCase(APITestCase):
    pass


class EventTestCase(APITestCase):
    pass


class StatusTestCase(APITestCase):
    pass
