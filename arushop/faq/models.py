from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Faq(models.Model):
    question = models.CharField(max_length=255)
    slug = models.SlugField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name="faq_likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="faq_dislikes", blank=True)
    views = models.ManyToManyField(User, related_name="faq_views", blank=True)
