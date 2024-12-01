from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from django.urls import path, include

schema_view = get_schema_view(
    title='Cache Monitoring API',
    description='API endpoints for cache monitoring and analysis',
    version='1.0',
    patterns=[
        path('api/v1/monitoring/', include('monitoring.urls')),
    ],
)

monitoring_api_docs = {
    'endpoints': {
        'dashboard_data': {
            'get': {
                'description': 'Retrieve real-time monitoring data',
                'parameters': [],
                'responses': {
                    '200': 'Successful response with monitoring data',
                    '403': 'Authentication required',
                }
            }
        },
        'export_data': {
            'get': {
                'description': 'Export monitoring data in various formats',
                'parameters': [
                    {'name': 'format', 'type': 'string', 'required': False},
                    {'name': 'from_date', 'type': 'string', 'required': False},
                    {'name': 'to_date', 'type': 'string', 'required': False},
                ],
                'responses': {
                    '200': 'Successful export',
                    '400': 'Invalid parameters',
                }
            }
        }
    }
}
