from django import template
from django.conf import settings
from ..monitoring import CacheMonitor
from ..alert_history import AlertHistory

register = template.Library()


@register.inclusion_tag('admin/tags/stats_panel.html')
def show_stats_panel():
    return {
        'cache_stats': CacheMonitor.get_cache_stats(),
        'refresh_interval': settings.MONITORING_DASHBOARD['REFRESH_INTERVAL']
    }


@register.inclusion_tag('admin/tags/alert_panel.html')
def show_alert_panel():
    return {
        'alerts': AlertHistory.get_recent_alerts(),
        'alert_limit': settings.MONITORING_DASHBOARD['ALERT_HISTORY_LIMIT']
    }
