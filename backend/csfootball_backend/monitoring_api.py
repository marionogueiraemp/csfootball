from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .monitoring import CacheMonitor
from .alert_history import AlertHistory
from .task_monitoring import TaskMonitor


class MonitoringAPIViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['GET'])
    def stats(self, request):
        return Response({
            'cache_stats': CacheMonitor.get_cache_stats(),
            'alert_stats': AlertHistory.get_alert_stats(),
            'task_stats': TaskMonitor.get_task_stats()
        })

    @action(detail=False, methods=['GET'])
    def performance(self, request):
        return Response({
            'cache_performance': CacheMonitor.get_performance_metrics(),
            'task_performance': TaskMonitor.get_performance_metrics()
        })
