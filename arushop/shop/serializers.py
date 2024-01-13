from rest_framework.serializers import ModelSerializer

from .models import Address, Cart, CartItem, Category, Product


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
