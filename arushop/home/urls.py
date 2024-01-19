from rest_framework import routers

from .views import BannersViewSet, BannerViewSet, ConfigViewSet, ShownCategoryViewSet, ShownProductViewSet

app_name = "home"

router = routers.DefaultRouter()
router.register(r"banner", BannerViewSet, basename="banner")
router.register(r"banners", BannersViewSet, basename="banners")
router.register(r"config", ConfigViewSet, basename="config")
router.register(r"shown_category", ShownCategoryViewSet, basename="shown_category")
router.register(r"shown_product", ShownProductViewSet, basename="shown_product")
