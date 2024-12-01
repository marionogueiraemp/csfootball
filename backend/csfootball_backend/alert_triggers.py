from django.core.cache import cache
from .notifications import TaskNotifications


class AlertTriggers:
    THRESHOLDS = {
        'cache_hit_rate': 70,  # Minimum acceptable hit rate percentage
        'memory_usage': 80,    # Maximum memory usage percentage
        'key_count': 10000     # Maximum number of cache keys
    }

    @staticmethod
    def check_cache_performance():
        stats = cache.get('monitoring:stats')
        if stats:
            hit_rate = (stats['hits'] /
                        (stats['hits'] + stats['misses'])) * 100
            if hit_rate < AlertTriggers.THRESHOLDS['cache_hit_rate']:
                TaskNotifications.send_alert(
                    'Low Cache Hit Rate',
                    f'Cache hit rate has dropped to {hit_rate:.2f}%'
                )

    @staticmethod
    def check_memory_usage():
        memory_usage = cache.info()['used_memory_percent']
        if memory_usage > AlertTriggers.THRESHOLDS['memory_usage']:
            TaskNotifications.send_alert(
                'High Memory Usage',
                f'Cache memory usage has reached {memory_usage}%'
            )
