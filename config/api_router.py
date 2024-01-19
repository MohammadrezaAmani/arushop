from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from arushop.blog.urls import router as blog_router
from arushop.faq.urls import router as faq_router
from arushop.other.urls import router as other_router
from arushop.shop.urls import router as shop_router
from arushop.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("user", UserViewSet)
router.registry.extend(shop_router.registry)
router.registry.extend(blog_router.registry)
router.registry.extend(other_router.registry)
router.registry.extend(other_router.registry)
router.registry.extend(faq_router.registry)


app_name = "api"
urlpatterns = router.urls
