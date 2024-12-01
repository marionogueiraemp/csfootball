from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


from datetime import datetime


def monitoring_api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        error_data = {
            'error': str(exc),
            'timestamp': datetime.now().isoformat(),
            'endpoint': context['request'].path
        }
        return Response(error_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
