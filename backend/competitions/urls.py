from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompetitionViewSet, MatchViewSet, PlayerStatsViewSet

router = DefaultRouter()
router.register(r'', CompetitionViewSet, basename='competition')
router.register(r'matches', MatchViewSet, basename='match')
router.register(r'player-stats', PlayerStatsViewSet, basename='player-stats')

urlpatterns = [
    path('', include(router.urls)),
    path('matches/<int:match_id>/player-stats/',
         PlayerStatsViewSet.as_view({'get': 'list'}),
         name='match-player-stats'),
]
