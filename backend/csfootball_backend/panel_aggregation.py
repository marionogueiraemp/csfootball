from django.core.cache import cache
from datetime import datetime, timedelta


class PanelDataAggregator:
    @staticmethod
    def aggregate_panel_stats(timeframe='1h'):
        stats = cache.get('panel_metrics:stats', [])
        return {
            'avg_hit_rate': sum(s['hit_rate'] for s in stats) / len(stats) if stats else 0,
            'peak_memory': max(s['memory_usage'] for s in stats) if stats else 0,
            'total_alerts': sum(s['alert_count'] for s in stats) if stats else 0,
            'timeframe': timeframe
        }

    @staticmethod
    def aggregate_performance_metrics():
        return {
            'response_times': PanelDataAggregator._get_response_times(),
            'error_rates': PanelDataAggregator._get_error_rates(),
            'cache_efficiency': PanelDataAggregator._get_cache_efficiency()
        }
