from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from functools import wraps
from .cache_keys import CacheKeyGenerator


def invalidate_cache(sender, instance, **kwargs):
    model_name = sender.__name__.lower()
    cache.delete_pattern(f"*:{model_name}:*")


def register_cache_invalidation(model):
    post_save.connect(invalidate_cache, sender=model)
    post_delete.connect(invalidate_cache, sender=model)


def cache_monitoring_response(timeout=300):  # 5 minutes default
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(self, request, *args, **kwargs):
            cache_key = CacheKeyGenerator.get_monitoring_key(
                endpoint=request.path,
                params=request.query_params
            )

            response = cache.get(cache_key)
            if response is None:
                response = view_func(self, request, *args, **kwargs)
                cache.set(cache_key, response, timeout=timeout)

            return response
        return wrapped_view
    return decorator


def cache_alert_response(timeout=60):  # 1 minute default
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(self, request, *args, **kwargs):
            cache_key = CacheKeyGenerator.get_alert_key(
                endpoint=request.path,
                params=request.query_params
            )

            response = cache.get(cache_key)
            if response is None:
                response = view_func(self, request, *args, **kwargs)
                cache.set(cache_key, response, timeout=timeout)

            return response
        return wrapped_view
    return decorator
