from django.conf import settings


class PanelConfig:
    @staticmethod
    def get_panel_settings():
        return {
            'refresh_interval': settings.MONITORING_DASHBOARD['REFRESH_INTERVAL'],
            'alert_limit': settings.MONITORING_DASHBOARD['ALERT_HISTORY_LIMIT'],
            'task_limit': settings.MONITORING_DASHBOARD['TASK_HISTORY_LIMIT']
        }

    @staticmethod
    def get_display_settings():
        return {
            'show_timestamps': True,
            'show_error_details': True,
            'compact_view': False
        }
