from datetime import datetime, timedelta


class CacheMonitoringAggregator:
    @staticmethod
    def aggregate_hourly_metrics(metrics):
        hourly_stats = {}

        for metric in metrics:
            hour = metric['timestamp'].replace(
                minute=0, second=0, microsecond=0)
            if hour not in hourly_stats:
                hourly_stats[hour] = {
                    'hits': 0,
                    'misses': 0,
                    'total_keys': 0,
                    'memory_usage': 0,
                    'count': 0
                }

            stats = hourly_stats[hour]
            stats['hits'] += metric['hits']
            stats['misses'] += metric['misses']
            stats['total_keys'] += metric['total_keys']
            stats['memory_usage'] += metric['memory_usage']
            stats['count'] += 1

        return hourly_stats

    @staticmethod
    def aggregate_key_stats(key_stats):
        return {
            'total_keys': len(key_stats),
            'total_size': sum(stat['size'] for stat in key_stats),
            'expiring_soon': len([s for s in key_stats if s['expires_at'] and s['expires_at'] < datetime.now() + timedelta(minutes=30)]),
            'largest_keys': sorted(key_stats, key=lambda x: x['size'], reverse=True)[:10]
        }
