from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from .api import AlertAPIViewSet, MonitoringAPIViewSet
from .views import MonitoringDashboardView
from competitions.views import MatchViewSet


router = DefaultRouter()
router.register(r'monitoring', MonitoringAPIViewSet, basename='monitoring')
router.register(r'alerts', AlertAPIViewSet, basename='alerts')
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/docs/', include_docs_urls(
        title='Cache Monitoring & Alert API',
        authentication_classes=[],
        permission_classes=[]
    )),
    path('api/users/', include('users.urls')),
    path('api/teams/', include('teams.urls')),
    path('api/competitions/', include('competitions.urls')),
    path('api/news/', include('news.urls')),
    path('api/forum/', include('forum.urls')),

    path('admin/', admin.site.urls),
    path('admin/monitoring/', MonitoringDashboardView.as_view(),
         name='monitoring-dashboard'),
]
