from django.core.cache import cache
from datetime import datetime


class PanelOptimizer:
    @staticmethod
    def optimize_panel_load():
        return {
            'cache_strategy': PanelOptimizer.determine_cache_strategy(),
            'refresh_interval': PanelOptimizer.calculate_optimal_refresh(),
            'data_compression': PanelOptimizer.should_compress_data()
        }

    @staticmethod
    def determine_cache_strategy():
        hit_rate = cache.get('panel_metrics:hit_rate', 0)
        return 'aggressive' if hit_rate < 70 else 'normal'

    @staticmethod
    def calculate_optimal_refresh():
        load_times = cache.get('panel_metrics:load_times', [])
        return max(30, min(300, sum(load_times) // len(load_times) if load_times else 60))
