from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Banner, Banners, Config, ShownCategory, ShownProduct
from .serializer import (
    BannerSerializer,
    BannersSerializer,
    ConfigSerializer,
    ShownCategorySerializer,
    ShownProductSerializer,
)


class BannerViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class BannersViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = BannersSerializer
    queryset = Banners.objects.all()


class ConfigViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ConfigSerializer
    queryset = Config.objects.all()


class ShownCategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ShownCategorySerializer
    queryset = ShownCategory.objects.all()


class ShownProductViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = ShownProductSerializer
    queryset = ShownProduct.objects.all()
