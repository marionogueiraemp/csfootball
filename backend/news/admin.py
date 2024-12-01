from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'article_type')
    search_fields = ('title', 'content')


# Only register if not already registered
if not admin.site.is_registered(Article):
    admin.site.register(Article, ArticleAdmin)
