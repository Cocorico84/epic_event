from typing import Any
from django.contrib.auth.models import AnonymousUser

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView
from app.models import Client, Contract, Event


class IsSales(BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        return request.user.is_authenticated and request.user.category == 'SALES'

    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        if request.method in SAFE_METHODS:
            return True

        if isinstance(obj, Client):
            return obj.client_contracts.filter(sales_contact=request.user).exists() # type: ignore
        elif isinstance(obj, Contract):
            return request.user == obj.sales_contact
        elif isinstance(obj, Event):
            return obj.client.client_contracts.filter(sales_contact=request.user).exists() # type: ignore
        return False


class IsSupport(BasePermission):
    def has_permission(self, request: Request, view) -> bool:
        if request.user.is_authenticated and request.user.category == 'SUPPORT':
            if view.basename == 'event':
                return True
            elif view.basename in ['contract', 'client']:
                if request.method == 'POST':
                    return False
                elif request.method == 'GET':
                    return True
        return False

    def has_object_permission(self, request: Request, view, obj: Any) -> bool:
        if isinstance(obj, Client) or isinstance(obj, Contract):
            return False
        return obj.client.client_events.filter(support_contact=request.user).exists()
