from django.core.cache import cache
from .cache_keys import CacheKeyGenerator


class CacheUtils:
    @staticmethod
    def clear_model_cache(model_name):
        cache.delete_pattern(f"*:{model_name}:*")

    @staticmethod
    def clear_instance_cache(model_name, instance_id):
        cache_key = CacheKeyGenerator.get_detail_key(model_name, instance_id)
        cache.delete(cache_key)

    @staticmethod
    def clear_related_cache(model_name, related_model, related_id):
        cache_key = CacheKeyGenerator.get_related_key(
            model_name, related_model, related_id)
        cache.delete(cache_key)

    @staticmethod
    def clear_all_cache():
        cache.clear()
