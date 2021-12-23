from rest_framework.serializers import ModelSerializer

from .models import Client, Contract, Event, Status
from users.models import CustomUser


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email', 'phone', 'company', 'date_updated', 'date_updated',)
        read_only_fields = ('date_created', 'date_updated',)


class ContractSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sales_contact'].queryset = CustomUser.objects.filter(category="SALES")

    class Meta:
        model = Contract
        fields = ('sales_contact', 'client', 'status', 'amount', 'payment_due', 'date_created', 'date_updated',)
        read_only_fields = ('date_created', 'date_updated')


class EventSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['support_contact'].queryset = CustomUser.objects.filter(category="SUPPORT")

    class Meta:
        model = Event
        fields = ('client', 'support_contact', 'event_status', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes',)
        read_only_fields = ('date_created', 'date_updated',)


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ('status',)
