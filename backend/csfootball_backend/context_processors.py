from .monitoring import CacheMonitor
from .alert_history import AlertHistory
from .task_monitoring import TaskMonitor


def monitoring_context(request):
    if request.user.is_staff:
        return {
            'monitoring_stats': {
                'cache': CacheMonitor.get_cache_stats(),
                'alerts': AlertHistory.get_recent_alerts(),
                'tasks': TaskMonitor.get_task_stats()
            }
        }
    return {}
