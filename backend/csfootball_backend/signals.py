from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


@receiver([post_save, post_delete])
def clear_cache_on_model_update(sender, instance, **kwargs):
    model_name = sender.__name__.lower()

    # Clear list view cache
    cache.delete_pattern(f"*/api/{model_name}s/*")

    # Clear detail view cache
    if hasattr(instance, 'id'):
        cache.delete_pattern(f"*/api/{model_name}s/{instance.id}/*")

    # Clear related caches
    if hasattr(instance, 'get_related_cache_keys'):
        related_keys = instance.get_related_cache_keys()
        for key in related_keys:
            cache.delete_pattern(key)
