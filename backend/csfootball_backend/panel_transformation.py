from datetime import datetime


class PanelDataTransformer:
    @staticmethod
    def transform_stats_data(raw_data):
        return {
            'hit_rate': round(raw_data['hit_rate'], 2),
            'memory_usage': f"{raw_data['memory_usage']}MB",
            'total_keys': int(raw_data['total_keys']),
            'last_updated': datetime.now().isoformat()
        }

    @staticmethod
    def transform_alert_data(raw_alerts):
        return [{
            'type': alert['type'],
            'message': alert['message'],
            'timestamp': datetime.fromisoformat(alert['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
            'severity': 'high' if alert['type'] == 'critical' else 'medium'
        } for alert in raw_alerts]
