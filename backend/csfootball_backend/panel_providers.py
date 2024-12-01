from .monitoring import CacheMonitor
from .alert_history import AlertHistory
from .task_monitoring import TaskMonitor


class PanelDataProvider:
    @staticmethod
    def get_stats_data():
        return {
            'cache': CacheMonitor.get_cache_stats(),
            'memory': CacheMonitor.get_memory_stats(),
            'keys': CacheMonitor.get_key_stats()
        }

    @staticmethod
    def get_alert_data():
        return {
            'recent': AlertHistory.get_recent_alerts(),
            'critical': AlertHistory.get_alerts_by_type('critical'),
            'warnings': AlertHistory.get_alerts_by_type('warning')
        }

    @staticmethod
    def get_task_data():
        return TaskMonitor.get_task_stats()
