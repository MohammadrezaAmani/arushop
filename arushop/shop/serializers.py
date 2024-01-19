from typing import Any

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Address, Cart, CartItem, Category, Product


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"

    def to_representation(self, instance: Any) -> dict[str, Any]:
        items = instance.cartitem_set.filter(active=True)
        data = super().to_representation(instance)
        data["items"] = CartItemSerializer(items, many=True).data
        # data["total"] = items.aggregate(total=Sum(F("product__actual_price") * F("quantity")))["total"]
        # data["discount"] = items.aggregate(total=Sum(F("product__price") * F("quantity")))["total"] - data["total"]
        # data['without_discount'] = items.aggregate(total=Sum(F('product__price') * F('quantity')))['total']
        return data


class CategorySerializer(ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        exclude = ["products"]

    def to_representation(self, instance: Any) -> dict[str, Any]:
        data = super().to_representation(instance)
        data["product_count"] = instance.products.count()
        return data


class ProductSerializer(ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    dislikes_count = serializers.IntegerField(read_only=True)
    views_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        exclude = ["likes", "dislikes", "views", "comments"]

    def to_representation(self, instance: Any) -> dict[str, Any]:
        data = super().to_representation(instance)
        data["images"] = list(map(lambda x: x.image.url, instance.images.all()))
        data["likes_count"] = instance.likes.count()
        data["dislikes_count"] = instance.dislikes.count()
        data["views_count"] = instance.views.count()
        data["comments_count"] = instance.comments.count()
        return data


class ProductMinimalSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ["likes", "dislikes", "views", "comments"]

    def to_representation(self, instance: Any) -> dict[str, Any]:
        data = super().to_representation(instance)
        data["images"] = list(map(lambda x: x.image.url, instance.images.all()))
        return data
