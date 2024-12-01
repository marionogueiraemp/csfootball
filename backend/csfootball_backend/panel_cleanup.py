from django.core.cache import cache
from datetime import datetime, timedelta


class PanelDataCleanup:
    @staticmethod
    def cleanup_old_data(days=30):
        cutoff_date = datetime.now() - timedelta(days=days)

        patterns_to_clean = [
            'panel_metrics:*',
            'panel_performance:*',
            'panel_analytics:*'
        ]

        cleaned_keys = 0
        for pattern in patterns_to_clean:
            keys = cache.keys(pattern)
            for key in keys:
                if PanelDataCleanup._is_old_data(key, cutoff_date):
                    cache.delete(key)
                    cleaned_keys += 1

        return {
            'cleaned_keys': cleaned_keys,
            'cutoff_date': cutoff_date.isoformat(),
            'timestamp': datetime.now().isoformat()
        }
