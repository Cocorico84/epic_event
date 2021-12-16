from rest_framework.viewsets import ModelViewSet

from .models import Contract, Event, Status
from .permissions import IsResponsibleOfContract, IsResponsibleOfEvent
from .serializers import ContractSerializer, EventSerializer, StatusSerializer


class ContractView(ModelViewSet):
    queryset = Contract.objects.all().order_by('-date_created')
    serializer_class = ContractSerializer
    permission_classes = [IsResponsibleOfContract]


class EventView(ModelViewSet):
    queryset = Event.objects.all().order_by('-date_created')
    serializer_class = EventSerializer
    permission_classes = [IsResponsibleOfEvent]


class StatusView(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = []
