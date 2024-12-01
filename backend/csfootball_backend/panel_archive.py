from django.core.cache import cache
from datetime import datetime
import json
import os


class PanelDataArchive:
    @staticmethod
    def archive_data(archive_name=None):
        if not archive_name:
            archive_name = f"panel_archive_{
                datetime.now().strftime('%Y%m%d_%H%M%S')}"

        archive_data = {
            'stats': cache.get('panel_metrics:stats', []),
            'alerts': cache.get('panel_metrics:alerts', []),
            'performance': cache.get('panel_metrics:performance', {}),
            'archived_at': datetime.now().isoformat()
        }

        archive_path = os.path.join('archives', f"{archive_name}.json")
        os.makedirs('archives', exist_ok=True)

        with open(archive_path, 'w') as f:
            json.dump(archive_data, f, indent=2)

        return {
            'status': 'success',
            'archive_name': archive_name,
            'archived_at': datetime.now().isoformat()
        }
