from django.contrib import admin
from news.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'article_type',
                    'created_at', 'is_published')
    list_filter = ('article_type', 'is_published')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
