from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(ReadOnlyModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.prefetch_related("products", "related").select_related("author", "category").all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    ordering_fields = ["created_at", "updated_at", "title"]
    search_fields = ["title", "content"]
    filterset_fields = ["title", "content"]
    http_method_names = ["get", "head", "options"]

    @action(detail=True, methods=["GET"])
    def like(self, request, slug=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post = self.get_object()
        post.likes.add(request.user)
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def dislike(self, request, slug=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post = self.get_object()
        post.dislikes.add(request.user)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def unlike(self, request, slug=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post = self.get_object()
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)
        return Response(status=status.HTTP_200_OK)
