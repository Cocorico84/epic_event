from rest_framework.viewsets import ModelViewSet

from .models import Client, Contract, Event, Status
from .permissions import IsSales, IsSupport
from .serializers import (ClientSerializer, ContractSerializer,
                          EventSerializer, StatusSerializer)


class ClientView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsSales | IsSupport]


class ContractView(ModelViewSet):
    queryset = Contract.objects.all().order_by('-date_created')
    serializer_class = ContractSerializer
    permission_classes = [IsSales | IsSupport]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class EventView(ModelViewSet):
    queryset = Event.objects.all().order_by('-date_created')
    serializer_class = EventSerializer
    permission_classes = [IsSales | IsSupport]

    def perform_create(self, serializer):
        if self.request.user.category == 'Support':
            serializer.save(support_contact=self.request.user)
        serializer.save()


class StatusView(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = []
