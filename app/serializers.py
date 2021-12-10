from rest_framework.serializers import ModelSerializer

from .models import Contract, Event, Status


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ('sales_contact', 'client', 'date_created', 'date_updated', 'status', 'amount', 'payment_due',)

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('client', 'support_contact', 'event_status', 'date_created', 'date_updated', 'attendees', 'event_date', 'notes',)

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('status',)
