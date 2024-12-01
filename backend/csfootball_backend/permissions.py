from rest_framework import permissions
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'ADMIN'


class IsLeagueManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'LEAGUE_MANAGER'


class IsNewsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'NEWS_MANAGER'


class IsTeamOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsCacheMonitor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class CacheMonitoringPermissions:
    def get_permissions(self):
        if self.action in ['stats', 'top_keys']:
            return [IsCacheMonitor()]
        elif self.action in ['clear', 'clear_expired']:
            return [IsCacheMonitor()]
        return [permissions.IsAdminUser()]


class MonitoringDashboardPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def handle_no_permission(self):
        raise PermissionDenied(
            "You do not have permission to access the monitoring dashboard.")


class MonitoringAPIPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class ReadOnlyMonitoringPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_staff
