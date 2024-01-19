from rest_framework.routers import DefaultRouter

from arushop.faq.views import FaqViewSet

router = DefaultRouter()
router.register("faq", FaqViewSet)
