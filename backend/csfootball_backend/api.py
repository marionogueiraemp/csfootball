from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .monitoring import CacheMonitor
from .cache import cache_monitoring_response
from .cache import cache_alert_response
from .analyzers import CacheMonitoringAnalyzer
from .alerts import CacheMonitoringAlerts
from .alert_history import AlertHistory


class MonitoringAPIViewSet(viewsets.ViewSet):
    @cache_monitoring_response(timeout=60)  # 1 minute cache for dashboard data
    @action(detail=False, methods=['GET'])
    def dashboard_data(self, request):
        metrics = CacheMonitor.get_cache_stats()
        analysis = CacheMonitoringAnalyzer.analyze_performance(metrics)
        alerts = CacheMonitoringAlerts.check_alerts(metrics)

        return Response({
            'metrics': metrics,
            'analysis': analysis,
            'alerts': alerts
        })

    @cache_monitoring_response(timeout=300)  # 5 minutes cache for export data
    @action(detail=False, methods=['GET'])
    def export_data(self, request):
        format = request.query_params.get('format', 'json')
        metrics = CacheMonitor.get_cache_stats()
        return CacheMonitor.export_data(metrics, format)


class AlertAPIViewSet(viewsets.ViewSet):
    @cache_alert_response(timeout=60)
    @action(detail=False, methods=['GET'])
    def alerts(self, request):
        hours = int(request.query_params.get('hours', 24))
        alerts = AlertHistory.get_recent_alerts(hours)
        return Response({
            'total': len(alerts),
            'critical': len([a for a in alerts if a['type'] == 'critical']),
            'alerts': alerts
        })

    @cache_alert_response(timeout=300)
    @action(detail=False, methods=['GET'])
    def stats(self, request):
        return Response({
            'cache_stats': CacheMonitor.get_cache_stats(),
            'recent_alerts': AlertHistory.get_recent_alerts(hours=1)
        })
