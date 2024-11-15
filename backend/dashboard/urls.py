from django.urls import path
from .views import AdminDashboardView, LeagueManagerDashboardView, NewsManagerDashboardView, TeamOwnerDashboardView, PlayerDashboardView

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('league-manager/', LeagueManagerDashboardView.as_view(),
         name='league-manager-dashboard'),
    path('news-manager/', NewsManagerDashboardView.as_view(),
         name='news-manager-dashboard'),
    path('team-owner/', TeamOwnerDashboardView.as_view(),
         name='team-owner-dashboard'),
    path('player/', PlayerDashboardView.as_view(), name='player-dashboard'),
]
