from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PlayerApplicationViewSet, TransferRequestViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'player-applications', PlayerApplicationViewSet,
                basename='player-application')
router.register(r'transfer-requests', TransferRequestViewSet,
                basename='transfer-request')

urlpatterns = [
    path('', include(router.urls)),
]
