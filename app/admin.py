from django.contrib import admin
from .models import Contract, Event, Status

admin.site.register(Contract)
admin.site.register(Event)
admin.site.register(Status)