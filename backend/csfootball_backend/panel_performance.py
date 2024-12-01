from django.core.cache import cache
from datetime import datetime, timedelta


class PanelPerformanceMonitor:
    @staticmethod
    def track_performance(panel_id):
        start_time = datetime.now()
        return lambda: PanelPerformanceMonitor._record_metrics(panel_id, start_time)

    @staticmethod
    def _record_metrics(panel_id, start_time):
        duration = (datetime.now() - start_time).total_seconds()
        cache.lpush(f'panel_performance:{panel_id}:times', duration)
        cache.ltrim(f'panel_performance:{panel_id}:times', 0, 999)

    @staticmethod
    def get_performance_stats(panel_id):
        times = cache.lrange(f'panel_performance:{panel_id}:times', 0, -1)
        return {
            'avg_load_time': sum(times) / len(times) if times else 0,
            'peak_load_time': max(times) if times else 0,
            'total_loads': len(times)
        }
