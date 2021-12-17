from django.contrib.auth.models import AbstractUser
from django.db import models

CATEGORIES = (
    ('SALES', 'SALES'),
    ('SUPPORT', 'SUPPORT'),
)


class CustomUser(AbstractUser):
    category = models.CharField(max_length=32, choices=CATEGORIES)
