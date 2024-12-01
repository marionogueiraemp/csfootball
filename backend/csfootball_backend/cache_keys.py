class CacheKeyGenerator:
    @staticmethod
    def get_list_key(model_name, user_id=None):
        return f"{model_name}:list:{user_id if user_id else 'all'}"

    @staticmethod
    def get_detail_key(model_name, id):
        return f"{model_name}:detail:{id}"

    @staticmethod
    def get_related_key(model_name, related_model, related_id):
        return f"related:{model_name}:{related_model}:{related_id}"

    @staticmethod
    def get_monitoring_key(endpoint, params):
        params_str = '_'.join(f"{k}:{v}" for k, v in sorted(params.items()))
        return f"monitoring:{endpoint}:{params_str}"

    @staticmethod
    def get_alert_key(endpoint, params):
        params_str = '_'.join(f"{k}:{v}" for k, v in sorted(params.items()))
        return f"alert:{endpoint}:{params_str}"

    @staticmethod
    def get_metrics_key(timestamp):
        return f"monitoring:metrics:{timestamp.strftime('%Y%m%d_%H%M')}"

    @staticmethod
    def get_analysis_key(metric_type):
        return f"monitoring:analysis:{metric_type}"
