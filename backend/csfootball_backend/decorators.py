from functools import wraps
from django.core.cache import cache
from django.db import models
from django.conf import settings
from rest_framework.renderers import JSONRenderer


def cache_response(timeout=settings.CACHE_TTL):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(self, request, *args, **kwargs):
            cache_key = f"{request.path}:{request.user.id}"
            cached_response = cache.get(cache_key)

            if cached_response is None:
                response = view_func(self, request, *args, **kwargs)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                cache.set(cache_key, response, timeout=timeout)
                return response

            return cached_response
        return _wrapped_view
    return decorator


def cache_model(timeout=None):
    def decorator(cls):
        model_name = f"Cached{cls.__name__}"

        class Meta:
            proxy = True
            app_label = cls._meta.app_label

        attrs = {
            'Meta': Meta,
            '__module__': cls.__module__,
            '_cached_original': cls,

            'save': lambda self, *args, **kwargs: (
                super(type(self), self).save(*args, **kwargs),
                cache.delete(f"{cls._meta.app_label}.{cls.__name__}.{self.pk}")
            )[0],

            'delete': lambda self, *args, **kwargs: (
                cache.delete(
                    f"{cls._meta.app_label}.{cls.__name__}.{self.pk}"),
                super(type(self), self).delete(*args, **kwargs)
            )[1],

            'get_cached': classmethod(lambda cls, pk: (
                cache.get(f"{cls._meta.app_label}.{cls._cached_original.__name__}.{pk}") or
                cls._cached_original.objects.get(pk=pk)
            ))
        }

        cached_model = type(model_name, (cls,), attrs)
        return cached_model

    return decorator
