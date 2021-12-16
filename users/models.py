from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = (
    ('Client', 'CLIENT'),
    ('Sale', 'SALES_CONTACT'),
    ('Support', 'SUPPORT_CONTACT'),
)


class CustomUser(AbstractUser):
    company = models.CharField(max_length=128, blank=True)
    category = models.CharField(max_length=32, choices=CATEGORIES)
