from rest_framework import serializers
from .models import ForumCategory, ForumThread, ForumPost


class ForumPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source='author.username', read_only=True)

    class Meta:
        model = ForumPost
        fields = ['id', 'thread', 'author', 'author_name', 'content',
                  'created_at', 'updated_at', 'is_edited']
        read_only_fields = ['author', 'is_edited']


class ForumThreadSerializer(serializers.ModelSerializer):
    creator_name = serializers.CharField(
        source='creator.username', read_only=True)
    posts = ForumPostSerializer(many=True, read_only=True)

    class Meta:
        model = ForumThread
        fields = ['id', 'title', 'category', 'creator', 'creator_name',
                  'created_at', 'is_pinned', 'is_locked', 'posts']
        read_only_fields = ['creator']


class ForumCategorySerializer(serializers.ModelSerializer):
    threads = ForumThreadSerializer(many=True, read_only=True)

    class Meta:
        model = ForumCategory
        fields = ['id', 'name', 'description', 'order', 'threads']
