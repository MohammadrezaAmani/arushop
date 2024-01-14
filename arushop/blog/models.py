from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from arushop.shop.models import Product, Category
from autoslug import AutoSlugField

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    content = MarkdownField(
        _("Content"), validator=VALIDATOR_STANDARD, rendered_field="rendered_content", null=True, blank=True
    )
    rendered_content = RenderedMarkdownField(null=True, blank=True)
    created = models.DateTimeField(_("Created"), default=timezone.now)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    publish = models.DateTimeField(_("Publish"), default=timezone.now)
    status = models.CharField(
        _("Status"), max_length=10, choices=(("draft", "Draft"), ("publish", "Publish"))
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )
    products = models.ManyToManyField(
        Product, verbose_name=_("Products"), blank=True, related_name="blog_products"
    )
    featured = models.BooleanField(_("Featured"), default=False)
    related = models.ManyToManyField(
        "self", verbose_name=_("Related posts"), blank=True
    )
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="blog_dislikes", blank=True)
    views = models.ManyToManyField(User, related_name="blog_views", blank=True)
    # comments = models.ManyToManyField(Comment, related_name="blog_comments", blank=True)
    
    class Meta:
        verbose_name = _("Blog post")
        verbose_name_plural = _("Blog posts")
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    @property
    def views_count(self):
        return self.views.count()
    
    @property
    def likes_count(self):
        return self.likes.count()
    
    @property
    def dislikes_count(self):
        return self.dislikes.count()
    
    @property
    def comments_count(self):
        return self.comments.count()