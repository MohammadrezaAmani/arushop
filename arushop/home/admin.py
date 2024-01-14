from django.contrib import admin
from .models import Slider, Sliders, Banner, Banners, ShownCategory, ShownProduct, ShownCategoryProduct, Config


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at', 'updated_at')
    search_fields = ['title', 'description', 'link']
    list_filter = ('created_at', 'updated_at')


class SlidersAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ('active', 'created_at', 'updated_at')


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'created_at', 'updated_at')
    search_fields = ['title', 'description', 'link']
    list_filter = ('created_at', 'updated_at')


class BannersAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ('active', 'created_at', 'updated_at')


class ShownCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ('active', 'created_at', 'updated_at')


class ShownProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ('active', 'created_at', 'updated_at')


class ShownCategoryProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ['name']
    list_filter = ('active', 'created_at', 'updated_at')


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_url', 'created_at', 'updated_at')
    search_fields = ['name', 'site_url']
    list_filter = ('created_at', 'updated_at')


# Register your models with the custom admin classes
admin.site.register(Slider, SliderAdmin)
admin.site.register(Sliders, SlidersAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Banners, BannersAdmin)
admin.site.register(ShownCategory, ShownCategoryAdmin)
admin.site.register(ShownProduct, ShownProductAdmin)
admin.site.register(ShownCategoryProduct, ShownCategoryProductAdmin)
admin.site.register(Config, ConfigAdmin)
