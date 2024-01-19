from typing import Any

from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from bases.viewsets import BaseViewSet

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(BaseViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.prefetch_related("user", "reply", "likes", "dislikes").all().order_by("-created")
    http_method_names = ["get", "post", "patch", "delete"]

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        request.data["user"] = request.user.id
        return super().create(request, *args, **kwargs)

    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        obj = self.get_object()
        if obj.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        obj = self.get_object()
        if obj.user != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)
