from rest_framework.serializers import ModelSerializer

from .models import Banner, Banners, Config, ShownCategory, ShownProduct


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class BannersSerializer(ModelSerializer):
    class Meta:
        model = Banners
        fields = "__all__"


class ConfigSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"


class ShownCategorySerializer(ModelSerializer):
    class Meta:
        model = ShownCategory
        fields = "__all__"


class ShownProductSerializer(ModelSerializer):
    class Meta:
        model = ShownProduct
        fields = "__all__"
