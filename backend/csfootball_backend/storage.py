
from django.core.cache import cache
from datetime import datetime, timedelta
import json


class CacheMonitoringStorage:
    METRICS_KEY = 'cache_monitoring:metrics'
    KEY_STATS_KEY = 'cache_monitoring:key_stats'

    @classmethod
    def store_metrics(cls, metrics):
        stored_metrics = cache.get(cls.METRICS_KEY, [])
        stored_metrics.append(metrics)

        # Keep last 24 hours of metrics
        cutoff_time = datetime.now() - timedelta(hours=24)
        stored_metrics = [
            m for m in stored_metrics if m['timestamp'] > cutoff_time]

        cache.set(cls.METRICS_KEY, stored_metrics)

    @classmethod
    def store_key_stats(cls, key_stats):
        cache.set(cls.KEY_STATS_KEY, key_stats)
