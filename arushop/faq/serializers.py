from rest_framework.serializers import ModelSerializer

from .models import Faq


class FaqSerailizer(ModelSerializer):
    class Meta:
        model = Faq
        exclude = ["likes", "dislikes", "views"]
