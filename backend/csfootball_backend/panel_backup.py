from django.core.cache import cache
from datetime import datetime
import json
import os


class PanelDataBackup:
    @staticmethod
    def create_backup():
        backup_data = {
            'stats': cache.get('panel_metrics:stats', []),
            'alerts': cache.get('panel_metrics:alerts', []),
            'performance': cache.get('panel_metrics:performance', {}),
            'timestamp': datetime.now().isoformat()
        }

        filename = f"panel_backup_{
            datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        backup_path = os.path.join('backups', filename)

        with open(backup_path, 'w') as f:
            json.dump(backup_data, f, indent=2)

        return {
            'status': 'success',
            'filename': filename,
            'timestamp': datetime.now().isoformat()
        }
