from celery import shared_task
from .invalidation import CacheInvalidationStrategy
from datetime import datetime


@shared_task
def cleanup_alert_cache():
    CacheInvalidationStrategy.invalidate_old_alerts(older_than_hours=24)
    return f"Alert cache cleanup completed at {datetime.now()}"


@shared_task
def cleanup_monitoring_cache():
    CacheInvalidationStrategy.invalidate_monitoring_cache()
    return f"Monitoring cache cleanup completed at {datetime.now()}"


@shared_task
def refresh_monitoring_analysis():
    CacheInvalidationStrategy.invalidate_analysis()
    return f"Analysis cache refreshed at {datetime.now()}"


@shared_task
def cleanup_expired_keys():
    CacheInvalidationStrategy.invalidate_alert_cache()
    CacheInvalidationStrategy.invalidate_monitoring_cache()
    return f"All expired keys cleaned up at {datetime.now()}"
