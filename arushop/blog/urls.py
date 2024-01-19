from rest_framework.routers import DefaultRouter

from arushop.blog.views import BlogPostViewSet

app_name = "blog"

router = DefaultRouter()
router.register("blog", BlogPostViewSet)
