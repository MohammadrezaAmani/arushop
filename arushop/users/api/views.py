from typing import Any

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

User = get_user_model()
from django.contrib.auth.models import AnonymousUser


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "phone"

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
