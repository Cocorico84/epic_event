from django.utils import timezone
from rest_framework.test import APITestCase
from users.models import CustomUser

from ..models import Client, Contract, Event, Status


class EpicTestCase(APITestCase):
    def setUp(self):
        self.client_test = Client.objects.create(
            first_name='harry',
            last_name='potter',
            email='hp@email.com',
            phone='1111',
            company='Poudlard',
        )
        self.sale = CustomUser.objects.create_user(username='sale', password='1234', category="Sale")
        self.sale_2 = CustomUser.objects.create_user(username='sale_2', password='1234', category="Sale")
        self.support = CustomUser.objects.create_user(username='support', password='1234', category="Support")
        self.support_2 = CustomUser.objects.create_user(username='support_2', password='1234', category="Support")

        self.contract = Contract.objects.create(
            sales_contact=self.sale,
            client=self.client_test,
            amount=10,
            payment_due=timezone.now()
        )
        self.status = Status.objects.create(status="In progress")
        self.event = Event.objects.create(
            client=self.client_test,
            support_contact=self.support,
            event_status=self.status,
            attendees=2,
        )
