from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
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

    @action(detail=False, methods=["get"])
    def _(self, request, *args, **kwargs):
        fields = self.request.GET.getlist("fields", None)
        queryset = self.get_queryset()
        serializer = self.get_serializer_class()
        data = serializer(queryset, many=True).data
        if fields:
            data = list(map(lambda x: {field: x[field] for field in fields if field in x}, data))
        return Response(data)

    @action(detail=True, methods=["get"])
    def __(self, request, *args, **kwargs):
        fields = self.request.GET.getlist("fields", None)
        obj = self.get_object()
        serializer = self.get_serializer_class()
        data = serializer(obj).data
        if fields:
            data = {field: data[field] for field in fields if field in data}
        return Response(data)
