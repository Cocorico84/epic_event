from rest_framework.viewsets import ModelViewSet
from .serializers import ContractSerializer, StatusSerializer, EventSerializer
from .models import Contract, Status, Event


class ContractView(ModelViewSet):
    queryset = Contract.objects.all().order_by('-date_created')
    serializer_class = ContractSerializer
    permission_classes = []


class EventView(ModelViewSet):
    queryset = Event.objects.all().order_by('-date_created')
    serializer_class = EventSerializer
    permission_classes = []


class StatusView(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = []
