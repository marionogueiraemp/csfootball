from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUser, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # JWT login
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
]
