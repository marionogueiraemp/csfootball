import csv
import json
from datetime import datetime
from django.http import HttpResponse


class CacheMonitoringExporter:
    @staticmethod
    def export_csv(metrics, key_stats):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="cache_stats_{
            datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Timestamp', 'Hits', 'Misses',
                        'Total Keys', 'Memory Usage'])

        for metric in metrics:
            writer.writerow([
                metric['timestamp'],
                metric['hits'],
                metric['misses'],
                metric['total_keys'],
                metric['memory_usage']
            ])

        return response

    @staticmethod
    def export_json(metrics, key_stats):
        data = {
            'metrics': metrics,
            'key_stats': key_stats,
            'exported_at': datetime.now().isoformat()
        }

        response = HttpResponse(json.dumps(
            data, indent=2), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename="cache_stats_{
            datetime.now().strftime("%Y%m%d_%H%M%S")}.json"'

        return response
