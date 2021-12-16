from typing import Any

from django.utils import timezone
from rest_framework.serializers import ModelSerializer

from .models import Contract, Event, Status


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = ('sales_contact', 'client', 'status', 'amount', 'payment_due', 'date_created', 'date_updated',)
        read_only_fields = ('date_created', 'date_updated',)

    def update(self, instance, validated_data: Any):
        instance.date_updated = timezone.now().date()
        return super().update(instance, validated_data)


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('client', 'support_contact', 'event_status', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes',)
        read_only_fields = ('date_created', 'date_updated',)

    def update(self, instance, validated_data: Any):
        instance.date_updated = timezone.now().date()
        return super().update(instance, validated_data)


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('status',)
