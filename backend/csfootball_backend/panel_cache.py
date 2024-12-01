from django.core.cache import cache
from datetime import datetime, timedelta


class PanelCache:
    @staticmethod
    def get_cached_panel_data(panel_id, user_id):
        cache_key = f"panel_data:{panel_id}:{user_id}"
        return cache.get(cache_key)

    @staticmethod
    def cache_panel_data(panel_id, user_id, data, timeout=300):
        cache_key = f"panel_data:{panel_id}:{user_id}"
        cache.set(cache_key, data, timeout=timeout)

    @staticmethod
    def invalidate_panel_cache(panel_id=None, user_id=None):
        if panel_id and user_id:
            cache.delete(f"panel_data:{panel_id}:{user_id}")
        elif panel_id:
            cache.delete_pattern(f"panel_data:{panel_id}:*")
        else:
            cache.delete_pattern("panel_data:*")
