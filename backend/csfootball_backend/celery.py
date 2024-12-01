from celery import Celery
from celery.schedules import crontab
from .notifications import TaskNotifications
from .task_reporting import TaskReporting
from datetime import datetime
from .alert_triggers import AlertTriggers

app = Celery('csfootball_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'cleanup-monitoring-cache': {
        'task': 'csfootball_backend.tasks.cleanup_monitoring_cache',
        'schedule': crontab(minute='*/30'),  # Every 30 minutes
    },
    'refresh-monitoring-analysis': {
        'task': 'csfootball_backend.tasks.refresh_monitoring_analysis',
        'schedule': crontab(minute='*/15'),  # Every 15 minutes
    },
    'cleanup-expired-keys': {
        'task': 'csfootball_backend.tasks.cleanup_expired_keys',
        'schedule': crontab(hour='*/12'),  # Every 12 hours
    },
    'send-daily-task-report': {
        'task': 'csfootball_backend.tasks.send_daily_report',
        'schedule': crontab(hour=23, minute=55),  # Send report at 23:55 daily
    },
    'cleanup-alert-cache': {
        'task': 'csfootball_backend.tasks.cleanup_alert_cache',
        'schedule': crontab(hour='*/1'),  # Every hour
    },
    'send-performance-alerts': {
        'task': 'csfootball_backend.tasks.check_and_send_alerts',
        'schedule': crontab(minute='*/15'),  # Check every 15 minutes
    }
}

app.conf.beat_schedule.update({
    'check-cache-performance': {
        'task': 'csfootball_backend.tasks.check_cache_performance',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
    'check-memory-usage': {
        'task': 'csfootball_backend.tasks.check_memory_usage',
        'schedule': crontab(minute='*/10'),  # Every 10 minutes
    }
})


@app.task
def send_daily_report():
    report = TaskReporting.generate_daily_report()
    TaskNotifications.send_task_report(report)
    return f"Daily report sent at {datetime.now()}"


@app.task
def check_cache_performance():
    AlertTriggers.check_cache_performance()


@app.task
def check_memory_usage():
    AlertTriggers.check_memory_usage()
