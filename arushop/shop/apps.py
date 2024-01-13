from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "arushop.shop"
    verbose_name = _("Shops")
