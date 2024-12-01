from datetime import datetime


class CacheMonitoringFormatter:
    @staticmethod
    def format_stats(stats):
        total = stats['hits'] + stats['misses']
        hit_rate = (stats['hits'] / total * 100) if total > 0 else 0

        return {
            'hits': stats['hits'],
            'misses': stats['misses'],
            'keys': stats['keys'],
            'size': stats['size'],
            'hit_rate': round(hit_rate, 2)
        }

    @staticmethod
    def format_key_stats(key_stats):
        return {
            'key': key_stats['key'],
            'hits': key_stats['hits'],
            'misses': key_stats['misses'],
            'size': key_stats['size'],
            'last_accessed': datetime.fromtimestamp(key_stats['last_accessed'])
        }
