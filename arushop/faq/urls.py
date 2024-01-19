from rest_framework.routers import DefaultRouter

from arushop.faq.views import FaqViewSet

app_name = "faq"

router = DefaultRouter()
router.register("faq", FaqViewSet)
