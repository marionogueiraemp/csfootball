from rest_framework.response import Response
from datetime import datetime


class MonitoringAPIResponseFormatter:
    @staticmethod
    def format_response(data, status=200):
        return Response({
            'data': data,
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'version': 'v1',
                'status': status
            }
        }, status=status)

    @staticmethod
    def format_error(message, code=400):
        return Response({
            'error': {
                'message': message,
                'code': code,
                'timestamp': datetime.now().isoformat()
            }
        }, status=code)


class AlertAPIResponseFormatter:
    @staticmethod
    def format_alert_response(alerts, status=200):
        return Response({
            'data': {
                'alerts': alerts,
                'metadata': {
                    'total_count': len(alerts),
                    'critical_count': len([a for a in alerts if a['type'] == 'critical']),
                    'timestamp': datetime.now().isoformat()
                }
            },
            'status': status
        })

    @staticmethod
    def format_error_response(message, status=400):
        return Response({
            'error': {
                'message': message,
                'timestamp': datetime.now().isoformat()
            },
            'status': status
        })
