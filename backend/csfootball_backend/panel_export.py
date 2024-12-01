import csv
import json
from datetime import datetime
from django.http import HttpResponse


class PanelDataExporter:
    @staticmethod
    def export_to_json(data):
        filename = f"panel_data_{
            datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        response = HttpResponse(json.dumps(
            data, indent=2), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

    @staticmethod
    def export_to_csv(data):
        filename = f"panel_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(['Timestamp', 'Metric', 'Value'])

        for metric, value in data.items():
            writer.writerow([datetime.now(), metric, value])

        return response
