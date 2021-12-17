from typing import Any

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView
from app.models import Client, Contract, Event
from users.models import CustomUser


class IsSales(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        sales = CustomUser.objects.filter(category='Sale')
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.user in sales:
                if isinstance(obj, Client):
                    return request.user in [contract.sales_contact for contract in obj.client_contracts.all()]
                elif isinstance(obj, Contract):
                    return request.user == obj.sales_contact
                elif isinstance(obj, Event):
                    return request.user in [contract.sales_contact for contract in obj.client.client_events.all()]


class IsSupport(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        supports = CustomUser.objects.filter(category='Support')
        if request.method in SAFE_METHODS:
            return True
        else:
            if isinstance(obj, Client) or isinstance(obj, Contract):
                return False
            return request.user in supports \
                and request.user in [event.support_contact for event in obj.client_events.all()]
