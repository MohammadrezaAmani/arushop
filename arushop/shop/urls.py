from rest_framework import routers

from .views import AddressViewSet, CartItemViewSet, CartViewSet, CategoryViewSet, ProductViewSet

app_name = "shop"

router = routers.DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")
router.register(r"address", AddressViewSet, basename="address")
router.register(r"cart", CartViewSet, basename="cart")
router.register(r"cartitem", CartItemViewSet, basename="cartitem")
router.register(r"category", CategoryViewSet, basename="category")
