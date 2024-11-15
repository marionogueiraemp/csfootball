from rest_framework import serializers
from .models import ForumSection, Thread, Post

class ForumSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumSection
        fields = ['id', 'title', 'description']

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'section', 'title', 'created_by', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'thread', 'content', 'created_by', 'created_at', 'updated_at']