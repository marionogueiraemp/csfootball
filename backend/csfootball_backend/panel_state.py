from django.core.cache import cache


class PanelState:
    @staticmethod
    def save_panel_state(user_id, panel_id, state):
        cache_key = f"panel_state:{user_id}:{panel_id}"
        cache.set(cache_key, state, timeout=3600)

    @staticmethod
    def get_panel_state(user_id, panel_id):
        cache_key = f"panel_state:{user_id}:{panel_id}"
        return cache.get(cache_key, {})

    @staticmethod
    def clear_panel_state(user_id):
        cache.delete_pattern(f"panel_state:{user_id}:*")
