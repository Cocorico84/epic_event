from django.conf import settings
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    company = models.CharField(max_length=32)
    date_updated = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE, related_name='sales_contact_contracts')
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='client_contracts')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateField()


class Status(models.Model):
    status = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self) -> str:
        return f"{self.status}"


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='client_events')
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                        on_delete=models.CASCADE, related_name='support_contact_events')
    event_status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    attendees = models.IntegerField()
    event_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
