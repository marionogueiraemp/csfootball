import json
import csv
from django.core.cache import cache
from .panel_validation import PanelDataValidator
from datetime import datetime


class PanelDataImporter:
    @staticmethod
    def import_from_json(json_file):
        data = json.load(json_file)
        PanelDataValidator.validate_stats_data(data)
        cache.set('panel_imported_data', data)
        return {
            'status': 'success',
            'imported_records': len(data),
            'timestamp': datetime.now().isoformat()
        }

    @staticmethod
    def import_from_csv(csv_file):
        data = {}
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data[row['Metric']] = row['Value']

        PanelDataValidator.validate_stats_data(data)
        cache.set('panel_imported_data', data)
        return {
            'status': 'success',
            'imported_records': len(data),
            'timestamp': datetime.now().isoformat()
        }
