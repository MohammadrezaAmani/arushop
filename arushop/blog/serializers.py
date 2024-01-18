from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        exclude = [
            "created",
            "updated",
            "publish",
            "status",
            "featured",
            "related",
            "likes",
            "dislikes",
            "views",
            "comments",
        ]
