from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ForumSectionViewSet, ThreadViewSet, PostViewSet

router = DefaultRouter()
router.register(r'forum-sections', ForumSectionViewSet)
router.register(r'threads', ThreadViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
