from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet

app_name = "comment"

router = routers.DefaultRouter()
router.register(r"comment", CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
]
