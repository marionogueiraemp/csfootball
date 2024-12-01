from rest_framework.schemas import AutoSchema
from rest_framework import permissions


class MonitoringAPISchema(AutoSchema):
    def get_description(self, path, method):
        if path.endswith('dashboard_data/'):
            return """
            Retrieves real-time cache monitoring data including:
            - Performance metrics (hits, misses, hit rate)
            - Memory usage statistics
            - Key statistics and analysis
            - Active alerts
            """
        elif path.endswith('export_data/'):
            return """
            Exports cache monitoring data in various formats:
            - JSON (default)
            - CSV
            - Excel
            
            Query Parameters:
            - format: Export format (json|csv|excel)
            - from_date: Start date for export
            - to_date: End date for export
            """
