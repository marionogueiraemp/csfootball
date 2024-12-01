from django.core.cache import cache
from datetime import datetime, timedelta


class CacheInvalidationStrategy:
    @staticmethod
    def invalidate_monitoring_cache():
        cache.delete_pattern('monitoring:*')

    @staticmethod
    def invalidate_metrics(older_than_hours=24):
        cutoff_time = datetime.now() - timedelta(hours=older_than_hours)
        keys_to_delete = []

        for key in cache.keys('monitoring:metrics:*'):
            timestamp = datetime.strptime(key.split(':')[-1], '%Y%m%d_%H%M')
            if timestamp < cutoff_time:
                keys_to_delete.append(key)

        cache.delete_many(keys_to_delete)

    @staticmethod
    def invalidate_analysis():
        cache.delete_pattern('monitoring:analysis:*')

    @staticmethod
    def invalidate_alert_cache():
        cache.delete_pattern('alert:*')

    @staticmethod
    def invalidate_old_alerts(older_than_hours=24):
        cutoff_time = datetime.now() - timedelta(hours=older_than_hours)
        keys_to_delete = []

        for key in cache.keys('alert:*'):
            timestamp = datetime.strptime(key.split(':')[-1], '%Y%m%d_%H%M')
            if timestamp < cutoff_time:
                keys_to_delete.append(key)

        cache.delete_many(keys_to_delete)
