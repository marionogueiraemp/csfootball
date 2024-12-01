from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .monitoring import CacheMonitor
from .permissions import CacheMonitoringPermissions, IsCacheMonitor
from .alert_history import AlertHistory
from .task_monitoring import TaskMonitor


class CacheMonitorViewSet(viewsets.ViewSet, CacheMonitoringPermissions):
    permission_classes = [IsCacheMonitor]

    @action(detail=False, methods=['GET'])
    def stats(self, request):
        return Response(CacheMonitor.get_cache_stats())

    @action(detail=False, methods=['GET'])
    def top_keys(self, request):
        return Response(CacheMonitor.get_top_keys())

    @action(detail=False, methods=['POST'])
    def clear(self, request):
        CacheMonitor.clear_all_cache()
        return Response({'status': 'success'})

    @action(detail=False, methods=['POST'])
    def clear_expired(self, request):
        CacheMonitor.clear_expired_keys()
        return Response({'status': 'success'})


@method_decorator(staff_member_required, name='dispatch')
class MonitoringDashboardView(TemplateView):
    template_name = 'admin/monitoring_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'cache_stats': CacheMonitor.get_cache_stats(),
            'recent_alerts': AlertHistory.get_recent_alerts(),
            'task_stats': TaskMonitor.get_task_stats()
        })
        return context
