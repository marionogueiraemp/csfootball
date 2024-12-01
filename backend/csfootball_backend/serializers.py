from rest_framework import serializers


class CacheStatsSerializer(serializers.Serializer):
    hit_rate = serializers.FloatField()
    memory_usage = serializers.IntegerField()
    total_keys = serializers.IntegerField()
    last_updated = serializers.DateTimeField()
    hits = serializers.IntegerField()
    misses = serializers.IntegerField()
    keys = serializers.IntegerField()
    size = serializers.IntegerField()
    hit_rate = serializers.FloatField()


class CacheKeyStatsSerializer(serializers.Serializer):
    key = serializers.CharField()
    hits = serializers.IntegerField()
    misses = serializers.IntegerField()
    size = serializers.IntegerField()
    last_accessed = serializers.DateTimeField()


class CacheMonitoringSerializer(serializers.Serializer):
    stats = CacheStatsSerializer()
    top_keys = CacheKeyStatsSerializer(many=True)


class AlertStatsSerializer(serializers.Serializer):
    total_alerts = serializers.IntegerField()
    critical_alerts = serializers.IntegerField()
    warning_alerts = serializers.IntegerField()
    last_alert = serializers.DateTimeField()


class TaskStatsSerializer(serializers.Serializer):
    success_rate = serializers.FloatField()
    total_tasks = serializers.IntegerField()
    failed_tasks = serializers.IntegerField()
    last_execution = serializers.DateTimeField()
