from django.conf import settings
from datetime import datetime
import pytz


class DashboardUtils:
    @staticmethod
    def format_timestamp(timestamp):
        tz = pytz.timezone(settings.MONITORING_DASHBOARD['DASHBOARD_TIMEZONE'])
        return timestamp.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_alert_class(alert_type):
        return {
            'critical': 'alert-danger',
            'warning': 'alert-warning',
            'info': 'alert-info'
        }.get(alert_type, 'alert-info')

    @staticmethod
    def format_memory_usage(bytes):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes < 1024:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024
