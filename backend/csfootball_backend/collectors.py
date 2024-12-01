from django.core.cache import cache
from datetime import datetime, timedelta
import json


class CacheDataCollector:
    @staticmethod
    def collect_performance_metrics():
        return {
            'hits': cache.get('cache_hits', 0),
            'misses': cache.get('cache_misses', 0),
            'total_keys': len(cache.keys('*')),
            'memory_usage': cache.info()['used_memory'],
            'timestamp': datetime.now()
        }

    @staticmethod
    def collect_key_metrics():
        all_keys = cache.keys('*')
        key_stats = []

        for key in all_keys:
            ttl = cache.ttl(key)
            value_size = len(json.dumps(cache.get(key)))

            key_stats.append({
                'key': key,
                'ttl': ttl,
                'size': value_size,
                'expires_at': datetime.now() + timedelta(seconds=ttl) if ttl > 0 else None
            })

        return key_stats
