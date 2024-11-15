from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsPostViewSet, InterviewViewSet, HistoricalEventViewSet

router = DefaultRouter()
router.register(r'news-posts', NewsPostViewSet)
router.register(r'interviews', InterviewViewSet)
router.register(r'historical-events', HistoricalEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
