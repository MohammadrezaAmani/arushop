from typing import Any
from django.contrib.auth import get_user_model
from rest_framework import serializers

from arushop.users.models import User as UserType, User
# for password
from django.contrib.auth.hashers import make_password
User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    # password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        exclude = ["is_staff", "is_superuser", "groups", "user_permissions", 'date_joined', 
        'is_active','last_login']
        # fields = '__all__'
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username", },
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
        representation.pop("password")
        return representation