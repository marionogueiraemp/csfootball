from django.core.cache import cache
import json
import os
from datetime import datetime
from .panel_validation import PanelDataValidator


class PanelDataRestore:
    @staticmethod
    def restore_from_backup(backup_file):
        with open(backup_file, 'r') as f:
            backup_data = json.load(f)

        PanelDataValidator.validate_stats_data(backup_data['stats'])

        cache.set('panel_metrics:stats', backup_data['stats'])
        cache.set('panel_metrics:alerts', backup_data['alerts'])
        cache.set('panel_metrics:performance', backup_data['performance'])

        return {
            'status': 'success',
            'restored_at': datetime.now().isoformat(),
            'backup_timestamp': backup_data['timestamp']
        }
