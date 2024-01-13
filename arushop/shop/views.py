from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Address, Cart, CartItem, Category
from .serializers import (
    AddressSerializer,
    CartItemSerializer,
    CartSerializer,
    CategorySerializer,
    Product,
    ProductSerializer,
)

User = get_user_model()


class BaseViewSet(ModelViewSet):
    serializer_class: serializers.BaseSerializer
    queryset: QuerySet

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


class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-created")

    @action(detail=True, methods=["get"])
    def category(self, request, pk=None):
        product = self.get_object()
        category = product.category_set.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class AddressViewSet(BaseViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all().order_by("-created")


class CartViewSet(BaseViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all().order_by("-date_added")


class CartItemViewSet(BaseViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all().order_by("-id")


class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("-created")

    @action(detail=True, methods=["get"])
    def products(self, request, *args, **kwargs):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
