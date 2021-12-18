from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Client, Contract, Event, Status
from .utils import EpicTestCase


class ClientTestCase(EpicTestCase):
    def setUp(self):
        super().setUp()
        refresh = RefreshToken.for_user(self.sale)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_get_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_client(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        data = {
            'first_name': 'al',
            'last_name': 'pacino',
            'phone': '789',
            'company': 'Movie',
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.count(), 1)
        self.client_test.refresh_from_db()
        self.assertEqual(self.client_test.first_name, "al")

    def test_update_with_another_sale(self):
        refresh = RefreshToken.for_user(self.sale_2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        data = {
            'first_name': 'al',
            'last_name': 'pacino',
            'phone': '789',
            'company': 'Movie',
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_client(self):
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)

    def test_delete_with_another_sale(self):
        refresh = RefreshToken.for_user(self.sale_2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        url = reverse('client-detail', kwargs={'pk': self.client_test.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ContractTestCase(EpicTestCase):
    def setUp(self):
        super().setUp()
        refresh = RefreshToken.for_user(self.sale)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_get_contract(self):
        url = reverse('contract-detail', kwargs={'pk': self.contract.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_contract(self):
        url = reverse('contract-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_contract(self):
        url = reverse('contract-list')
        data = {
            "client": self.client_test.pk,
            "amount": 10,
            "payment_due": timezone.now().date()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contract.objects.count(), 2)

    def test_update_contract(self):
        url = reverse('contract-detail', kwargs={'pk': self.contract.pk})
        data = {
            "amount": 42
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contract.objects.count(), 1)
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.amount, 42)

    def test_update_contract_with_another_sale(self):
        refresh = RefreshToken.for_user(self.sale_2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        url = reverse('contract-detail', kwargs={'pk': self.contract.pk})
        data = {
            "amount": 42
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Contract.objects.count(), 1)
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.amount, 10)

    def test_delete_contract(self):
        url = reverse('contract-detail', kwargs={'pk': self.contract.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Contract.objects.count(), 0)

    def test_delete_contract_with_another_sale(self):
        refresh = RefreshToken.for_user(self.sale_2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        url = reverse('contract-detail', kwargs={'pk': self.contract.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Contract.objects.count(), 1)


class EventTestCase(EpicTestCase):
    def setUp(self):
        super().setUp()
        refresh = RefreshToken.for_user(self.sale)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_get_event(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_event(self):
        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self):
        url = reverse('event-list')
        data = {
            "client": self.client_test.pk,
            "support_contact": self.support.pk,
            "event_status": self.status.id,
            "attendees": 2,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 2)

    def test_update_event(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        data = {
            "attendees": 42
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.count(), 1)
        self.event.refresh_from_db()
        self.assertEqual(self.event.attendees, 42)

    def test_update_event_with_another_sale(self):
        refresh = RefreshToken.for_user(self.sale_2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        data = {
            "attendees": 42
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.event.refresh_from_db()
        self.assertEqual(self.event.attendees, 2)

    def test_delete_event(self):
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Event.objects.count(), 0)

    def test_delete_event_with_another_sale(self):
        refresh = RefreshToken.for_user(self.sale_2)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        url = reverse('event-detail', kwargs={'pk': self.event.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Event.objects.count(), 1)


class StatusTestCase(EpicTestCase):
    def setUp(self):
        super().setUp()
        refresh = RefreshToken.for_user(self.sale)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_get_status(self):
        url = reverse('status-detail', kwargs={'pk': self.status.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_status(self):
        url = reverse('status-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_status(self):
        url = reverse('status-list')
        data = {
            "status": "done"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 2)

    def test_update_status(self):
        url = reverse('status-detail', kwargs={'pk': self.status.pk})
        data = {
            "status": "to do"
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Status.objects.count(), 1)
        self.status.refresh_from_db()
        self.assertEqual(self.status.status, "to do")

    def test_delete_status(self):
        url = reverse('status-detail', kwargs={'pk': self.status.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Status.objects.count(), 0)
