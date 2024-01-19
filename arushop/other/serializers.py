from rest_framework.serializers import ModelSerializer

from .models import Comment, Image


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["likes", "dislikes"]


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
