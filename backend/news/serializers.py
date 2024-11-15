from rest_framework import serializers
from .models import NewsPost, Interview, HistoricalEvent

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['id', 'title', 'content', 'created_at', 'author']

class HistoricalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEvent
        fields = ['id', 'event_title', 'event_description', 'event_date']