from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from django.urls import path, include

schema_view = get_schema_view(
    title='Cache Alert API',
    description='API endpoints for cache monitoring alerts',
    version='1.0',
    patterns=[
        path('api/v1/monitoring/alerts/', include('alerts.urls')),
    ],
)

alert_api_docs = {
    'endpoints': {
        'alerts': {
            'get': {
                'description': 'Retrieve alert history',
                'parameters': [
                    {'name': 'hours', 'type': 'integer', 'required': False},
                    {'name': 'type', 'type': 'string', 'required': False},
                ],
                'responses': {
                    '200': 'List of alerts',
                    '403': 'Authentication required',
                }
            }
        },
        'stats': {
            'get': {
                'description': 'Retrieve alert statistics',
                'parameters': [],
                'responses': {
                    '200': 'Alert statistics',
                    '403': 'Authentication required',
                }
            }
        }
    }
}
