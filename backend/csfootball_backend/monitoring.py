from django.core.cache import cache
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class CacheMonitor:
    @staticmethod
    def log_cache_hit(cache_key):
        logger.info(f"Cache hit: {cache_key} at {datetime.now()}")

    @staticmethod
    def log_cache_miss(cache_key):
        logger.info(f"Cache miss: {cache_key} at {datetime.now()}")

    @staticmethod
    def get_cache_stats():
        stats = {
            'hits': cache.get('cache_hits', 0),
            'misses': cache.get('cache_misses', 0),
            'keys': len(cache.keys('*')),
        }
        return stats
