from typing import Any

from django.contrib.auth import get_user_model

# for password
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from arushop.users.models import User
from arushop.users.models import User as UserType

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]
        extra_kwargs = {
            "url": {
                "view_name": "api:user-detail",
                "lookup_field": "username",
            },
        }


class UserDetailSerializer(serializers.ModelSerializer[UserType]):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "password", "last_login", "date_joined"]

        extra_kwargs = {
            "url": {
                "view_name": "api:user-detail",
                "lookup_field": "username",
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.password = make_password(validated_data["password"])
        return user

    def update(self, instance: User, validated_data: Any) -> User:
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)

    def to_representation(self, instance: User) -> Any:
        representation = super().to_representation(instance)
        representation["is_staff"] = instance.is_staff
        return representation
