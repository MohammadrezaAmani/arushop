from django.contrib import admin
from django.contrib.auth import get_user_model

admin.site.register(get_user_model())
# User = get_user_model()

# # if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
# #     # Force the `admin` sign in process to go through the `django-allauth` workflow:
# #     # https://django-allauth.readthedocs.io/en/stable/advanced.html#admin
# #     admin.site.login = decorators.login_required(admin.site.login)  # type: ignore[method-assign]


# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         (_("Personal info"), {"fields": ("name", "email")}),
#         (
#             _("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (_("Important dates"), {"fields": ("last_login", "date_joined")}),
#     )
#     list_display = ["username", "name", "is_superuser"]
#     search_fields = ["name"]
