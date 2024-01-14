import random

from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from arushop.shop.models import Category, Product
from arushop.other.models import Comment, Image

class Slider(models.Model):
    image = models.ImageField(upload_to="slider")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def random_slider(self, number: int = 1):
        return random.choices(self.objects.all(), k=number)

    def get_absolute_url(self):
        return self.link

    def get_image(self):
        return self.image.url


class Sliders(models.Model):
    sliders = models.ManyToManyField(Slider)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def radnom_slider(self):
        return random.choice(self.sliders.all())


class Banner(models.Model):
    image = models.ImageField(upload_to="banner")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def random_banner(self, number: int = 1):
        return random.choices(self.objects.all(), k=number)

    def get_absolute_url(self):
        return self.link

    def get_image(self):
        return self.image.url


class Banners(models.Model):
    banners = models.ManyToManyField(Banner)
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def radnom_banner(self):
        return random.choice(self.banners.all())


class ShownCategory(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.category.get_absolute_url()

    def get_image(self):
        return self.category.image.url

    def random_category(self, number: int = 1):
        return random.choices(self.category.all(), k=number)


class ShownProduct(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def get_image(self):
        return self.product.image.url

    def random_product(self, number: int = 1):
        return random.choices(self.product.all(), k=number)


class ShownCategoryProduct(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.category.get_absolute_url()

    def get_image(self):
        return self.category.image.url

    def random_category(self, number: int = 1):
        return random.choices(self.category.all(), k=number)


class Config(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    about = MarkdownField(rendered_field='about_rendered', validator=VALIDATOR_STANDARD,null=True, blank=True)
    about_rendered = RenderedMarkdownField(null=True, blank=True)
    site_url = models.CharField(max_length=256, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
