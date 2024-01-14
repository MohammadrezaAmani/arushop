from django.contrib import admin

from .models import Address, Cart, CartItem, Category, Comment, Product

admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
