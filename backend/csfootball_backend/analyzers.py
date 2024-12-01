from datetime import datetime, timedelta


class CacheMonitoringAnalyzer:
    @staticmethod
    def analyze_performance(metrics):
        return {
            'hit_rate': CacheMonitoringAnalyzer.calculate_hit_rate(metrics),
            'memory_trend': CacheMonitoringAnalyzer.analyze_memory_trend(metrics),
            'peak_usage': CacheMonitoringAnalyzer.find_peak_usage(metrics),
            'recommendations': CacheMonitoringAnalyzer.generate_recommendations(metrics)
        }

    @staticmethod
    def calculate_hit_rate(metrics):
        total_hits = sum(m['hits'] for m in metrics)
        total_misses = sum(m['misses'] for m in metrics)
        return (total_hits / (total_hits + total_misses)) * 100 if (total_hits + total_misses) > 0 else 0

    @staticmethod
    def analyze_memory_trend(metrics):
        memory_values = [m['memory_usage'] for m in metrics]
        trend = 'increasing' if memory_values[-1] > memory_values[0] else 'decreasing'
        return {
            'trend': trend,
            'growth_rate': (memory_values[-1] - memory_values[0]) / len(metrics)
        }

    @staticmethod
    @staticmethod
    def generate_recommendations(metrics):
        recommendations = []
        hit_rate = CacheMonitoringAnalyzer.calculate_hit_rate(metrics)

        if hit_rate < 70:
            recommendations.append("Consider increasing cache TTL")
        if CacheMonitoringAnalyzer.analyze_memory_trend(metrics)['trend'] == 'increasing':
            recommendations.append("Monitor memory usage growth")

        return recommendations
