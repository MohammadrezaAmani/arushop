from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from arushop.other.serializers import CommentSerializer, ImageSerializer
from arushop.users.api.serializers import UserSerializer
from bases.viewsets import BaseViewSet

from .models import Address, Cart, CartItem, Category
from .serializers import (
    AddressSerializer,
    CartItemSerializer,
    CartSerializer,
    CategorySerializer,
    Product,
    ProductMinimalSerializer,
    ProductSerializer,
)

User = get_user_model()

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet


class ProductViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    queryset = (
        Product.objects.prefetch_related("likes", "dislikes", "views", "comments", "images").all().order_by("-created")
    )

    @action(detail=True, methods=["get"])
    def category(self, request, pk=None):
        product = self.get_object()
        category = product.category_set.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def comments(self, request, pk=None):
        product = self.get_object()
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def images(self, request, pk=None):
        product = self.get_object()
        images = product.images.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def likes(self, request, pk=None):
        product = self.get_object()
        likes = product.likes.all()
        serializer = UserSerializer(likes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def dislikes(self, request, pk=None):
        product = self.get_object()
        dislikes = product.dislikes.all()
        serializer = UserSerializer(dislikes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def like(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        product = self.get_object()
        product.likes.add(request.user)
        if request.user in product.dislikes.all():
            product.dislikes.remove(request.user)
        product.save()
        return Response(status=200)

    @action(detail=True, methods=["get"])
    def dislike(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        product = self.get_object()
        product.dislikes.add(request.user)
        # remove from likes
        if request.user in product.likes.all():
            product.likes.remove(request.user)
        product.save()
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def comment(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        product = self.get_object()
        request.data["user"] = request.user.id
        request.data["product"] = product.id
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer["product"] = product
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["post"])
    def add_to_cart(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product = self.get_object()
        cart = Cart.objects.filter(user=request.user).first()
        quantity = request.data.get("quantity", 1)
        if not cart:
            cart = Cart.objects.create(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if not cart_item:
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        cart_item.quantity = quantity
        cart_item.save()
        return Response(status=200)

    @action(detail=True, methods=["post"])
    def remove_from_cart(self, request, pk=None):
        if isinstance(request.user, AnonymousUser):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product = self.get_object()
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return Response(status=200)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if not cart_item:
            return Response(status=200)
        cart_item.delete()
        return Response(status=200)


class AddressViewSet(BaseViewSet):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    serializer_class = AddressSerializer
    queryset = Address.objects.all().order_by("-created")


class CartViewSet(BaseViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all().order_by("-date_added")

    @action(detail=True, methods=["get"])
    def items(self, request, pk=None):
        cart = self.get_object()
        items = cart.cartitem_set.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def total(self, request, pk=None):
        cart = self.get_object()
        return Response(cart.total)

    @action(detail=True, methods=["get"])
    def user(self, request, pk=None):
        cart = self.get_object()
        return Response(cart.user)


class CartItemViewSet(BaseViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all().order_by("-id")


class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().prefetch_related("products", "products__images").order_by("-created")

    @action(detail=True, methods=["get"])
    def products(self, request, *args, **kwargs):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductMinimalSerializer(products, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def product_count(self, request, *args, **kwargs):
        category = self.get_object()
        return Response(category.products.count())


@api_view(["GET"])
def me(request):
    if request.user:
        return Response(request.user.username)
    return Response("Anonymous")
