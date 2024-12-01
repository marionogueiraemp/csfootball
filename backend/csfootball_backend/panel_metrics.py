from django.core.cache import cache
from datetime import datetime, timedelta


class PanelMetrics:
    @staticmethod
    def record_panel_access(panel_id):
        key = f"panel_metrics:access:{panel_id}"
        cache.incr(key)

    @staticmethod
    def record_panel_load_time(panel_id, load_time):
        key = f"panel_metrics:load_time:{panel_id}"
        cache.lpush(key, load_time)
        cache.ltrim(key, 0, 99)  # Keep last 100 measurements

    @staticmethod
    def get_panel_stats(panel_id):
        return {
            'access_count': int(cache.get(f"panel_metrics:access:{panel_id}", 0)),
            'avg_load_time': PanelMetrics.calculate_avg_load_time(panel_id),
            'last_accessed': cache.get(f"panel_metrics:last_access:{panel_id}")
        }
