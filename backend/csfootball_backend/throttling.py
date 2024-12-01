from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class MonitoringAPIThrottle(UserRateThrottle):
    rate = '60/minute'

    def get_cache_key(self, request, view):
        if request.user.is_staff:
            return None  # No throttling for staff users
        return super().get_cache_key(request, view)


class MonitoringExportThrottle(UserRateThrottle):
    rate = '10/hour'  # Limit export requests


class AlertAPIThrottle(UserRateThrottle):
    rate = '60/minute'  # 60 requests per minute

    def get_cache_key(self, request, view):
        if request.user.is_staff:
            return None  # No throttling for staff users
        return super().get_cache_key(request, view)


class AlertExportThrottle(UserRateThrottle):
    rate = '10/hour'  # 10 export requests per hour


class MonitoringUserThrottle(UserRateThrottle):
    rate = '100/minute'

    def get_cache_key(self, request, view):
        if request.user.is_staff:
            return None
        return super().get_cache_key(request, view)


class MonitoringAnonThrottle(AnonRateThrottle):
    rate = '20/minute'
