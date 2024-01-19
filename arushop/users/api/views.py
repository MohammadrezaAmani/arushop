from typing import Any

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import DetailSerializerMixin

from .serializers import UserDetailSerializer, UserSerializer

User = get_user_model()
from django.contrib.auth.models import AnonymousUser


class UserViewSet(DetailSerializerMixin, ModelViewSet):
    serializer_class = UserSerializer
    serializer_detail_class = UserDetailSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=False)
    def me(self, request):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if request.user.username != kwargs["username"]:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserDetailSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if request.user.username != kwargs["username"]:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = UserDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
