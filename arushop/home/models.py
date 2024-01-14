from django.db import models

from arushop.shop.models import (
    Address,
    Cart,
    CartItem,
    Category,
    Product,
    Comment,
)

class Slider(models.Model):
    image = models.ImageField(upload_to="slider")
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    time = models.TimeField(defualt="00:00:50")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Sliders(models.Model):
    sliders = models.ManyToManyField(Slider)
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name