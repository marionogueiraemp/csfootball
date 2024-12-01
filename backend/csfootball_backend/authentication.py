from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed


class MonitoringAPIAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not user.is_staff:
            raise AuthenticationFailed(
                'Only staff members can access monitoring API')
        return user, token


class ReadOnlyMonitoringAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not user.is_authenticated:
            raise AuthenticationFailed(
                'Authentication required for monitoring API')
        return user, token


class MonitoringAPIPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class AlertAPIAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if not user.is_staff:
            raise AuthenticationFailed(
                'Only staff members can access alert API')
        return user, token


class AlertAPIPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
