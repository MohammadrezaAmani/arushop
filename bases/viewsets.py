from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class BaseViewSet(ModelViewSet):
    serializer_class: serializers.BaseSerializer
    queryset: QuerySet
    pagination_class = StandardResultsSetPagination
    http_method_names = ["get"]
