from celery.signals import task_success, task_failure, task_retry
from datetime import datetime
from django.core.cache import cache


class TaskMonitor:
    @staticmethod
    @task_success.connect
    def task_success_handler(sender=None, **kwargs):
        cache.incr('monitoring:tasks:success')
        cache.lpush('monitoring:tasks:history', {
            'task': sender.name,
            'status': 'success',
            'timestamp': datetime.now().isoformat()
        })

    @staticmethod
    @task_failure.connect
    def task_failure_handler(sender=None, exception=None, **kwargs):
        cache.incr('monitoring:tasks:failure')
        cache.lpush('monitoring:tasks:history', {
            'task': sender.name,
            'status': 'failure',
            'error': str(exception),
            'timestamp': datetime.now().isoformat()
        })

    @staticmethod
    def get_task_stats():
        return {
            'success_count': int(cache.get('monitoring:tasks:success', 0)),
            'failure_count': int(cache.get('monitoring:tasks:failure', 0)),
            'history': cache.lrange('monitoring:tasks:history', 0, 50)
        }
