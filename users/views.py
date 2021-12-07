from rest_framework import serializers
from rest_framework.generics import CreateAPIView

from users.models import CustomUser

from .serializers import CustomUserSerializer


class CustomUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
