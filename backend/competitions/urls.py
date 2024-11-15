from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompetitionViewSet, MatchViewSet, PlayerStatsViewSet

router = DefaultRouter()
router.register(r'competitions', CompetitionViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'player-stats', PlayerStatsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
