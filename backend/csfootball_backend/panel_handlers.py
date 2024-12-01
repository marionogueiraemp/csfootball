from django.core.cache import cache
from .panel_providers import PanelDataProvider
from .task_monitoring import TaskMonitor
from alert_history import AlertHistory


class PanelEventHandler:
    @staticmethod
    def handle_refresh():
        return {
            'stats': PanelDataProvider.get_stats_data(),
            'alerts': PanelDataProvider.get_alert_data(),
            'tasks': PanelDataProvider.get_task_data()
        }

    @staticmethod
    def handle_alert_click(alert_id):
        return AlertHistory.get_alert_details(alert_id)

    @staticmethod
    def handle_task_filter(status):
        return TaskMonitor.get_filtered_tasks(status)
