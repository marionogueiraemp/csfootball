from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta


class CacheMonitoringAlerts:
    ALERT_THRESHOLDS = {
        'hit_rate_low': 50,  # percentage
        'memory_usage_high': 80,  # percentage
        'key_count_high': 10000
    }

    @staticmethod
    def check_alerts(metrics):
        alerts = []

        if CacheMonitoringAlerts.check_hit_rate(metrics):
            alerts.append("Low cache hit rate detected")

        if CacheMonitoringAlerts.check_memory_usage(metrics):
            alerts.append("High memory usage detected")

        if CacheMonitoringAlerts.check_key_count(metrics):
            alerts.append("High number of cache keys detected")

        if alerts:
            CacheMonitoringAlerts.send_alert_notification(alerts)

    @staticmethod
    def send_alert_notification(alerts):
        subject = 'Cache Monitoring Alert'
        message = '\n'.join(alerts)
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin[1] for admin in settings.ADMINS],
            fail_silently=False,
        )
