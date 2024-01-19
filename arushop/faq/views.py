from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Faq
from .serializers import FaqSerailizer


class FaqViewSet(ReadOnlyModelViewSet):
    serializer_class = FaqSerailizer
    queryset = Faq.objects.all()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    ordering_fields = ["created_at", "updated_at", "question"]
    search_fields = ["question", "answer"]
    filterset_fields = ["question", "answer"]
    http_method_names = ["get", "head", "options"]

    @action(detail=True, methods=["GET"])
    def like(self, request, slug=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        faq = self.get_object()
        faq.likes.add(request.user)
        if request.user in faq.dislikes.all():
            faq.dislikes.remove(request.user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def dislike(self, request, slug=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        faq = self.get_object()
        faq.dislikes.add(request.user)
        if request.user in faq.likes.all():
            faq.likes.remove(request.user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def unlike(self, request, slug=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        faq = self.get_object()
        if request.user in faq.likes.all():
            faq.likes.remove(request.user)
        if request.user in faq.dislikes.all():
            faq.dislikes.remove(request.user)
        return Response(status=status.HTTP_200_OK)
