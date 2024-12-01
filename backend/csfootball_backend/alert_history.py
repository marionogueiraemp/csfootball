from django.core.cache import cache
from datetime import datetime, timedelta


class AlertHistory:
    HISTORY_KEY = 'monitoring:alert_history'
    MAX_HISTORY_SIZE = 100

    @staticmethod
    def add_alert(alert_type, message):
        alert = {
            'type': alert_type,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }

        history = cache.get(AlertHistory.HISTORY_KEY, [])
        history.insert(0, alert)

        if len(history) > AlertHistory.MAX_HISTORY_SIZE:
            history = history[:AlertHistory.MAX_HISTORY_SIZE]

        cache.set(AlertHistory.HISTORY_KEY, history)

    @staticmethod
    def get_recent_alerts(hours=24):
        history = cache.get(AlertHistory.HISTORY_KEY, [])
        cutoff = datetime.now() - timedelta(hours=hours)

        return [
            alert for alert in history
            if datetime.fromisoformat(alert['timestamp']) > cutoff
        ]
