from django.core.exceptions import ValidationError
from datetime import datetime


class PanelDataValidator:
    @staticmethod
    def validate_stats_data(data):
        required_fields = ['hit_rate', 'memory_usage', 'total_keys']
        if not all(field in data for field in required_fields):
            raise ValidationError("Missing required stats fields")

        if not (0 <= data['hit_rate'] <= 100):
            raise ValidationError("Hit rate must be between 0 and 100")

    @staticmethod
    def validate_alert_data(data):
        required_fields = ['type', 'message', 'timestamp']
        if not all(field in data for field in required_fields):
            raise ValidationError("Missing required alert fields")

        if data['type'] not in ['critical', 'warning', 'info']:
            raise ValidationError("Invalid alert type")
