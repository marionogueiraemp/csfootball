from django.contrib import admin
from django.core.cache import cache
from django.urls import path
from django.http import JsonResponse
from django.template.response import TemplateResponse
from .monitoring import CacheMonitor


class CacheAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('cache-stats/', self.admin_site.admin_view(self.cache_stats_view),
                 name='cache-stats'),
            path('clear-cache/', self.admin_site.admin_view(self.clear_cache_view),
                 name='clear-cache'),
        ]
        return custom_urls + urls

    def cache_stats_view(self, request):
        stats = CacheMonitor.get_cache_stats()
        return JsonResponse(stats)

    def clear_cache_view(self, request):
        cache.clear()
        return JsonResponse({'status': 'success'})
