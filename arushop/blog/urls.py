from rest_framework.routers import DefaultRouter

from arushop.blog.views import BlogPostViewSet

router = DefaultRouter()
router.register("blog", BlogPostViewSet)
