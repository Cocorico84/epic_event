from django.conf import settings
from django.db import models


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales_contact_contracts')
    client = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_contracts')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField()
    status = models.BooleanField()
    amount = models.FloatField()
    payment_due = models.DateField()


class Status(models.Model):
    status = models.CharField(max_length=64)


class Event(models.Model):
    client = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_events')
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='support_contact_events')
    event_status = models.OneToOneField(Status, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField()
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField()
