from typing import Any

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField, ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'required': True}}

    def validate(self, attrs: Any) -> Any:
        if attrs['confirm_password'] != attrs['password']:
            raise ValidationError("The passwords didn't match")
        return super().validate(attrs)

    def create(self, validated_data: Any) -> Any:
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
