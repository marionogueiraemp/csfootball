from django.contrib import admin
from .models import ForumCategory, ForumThread, ForumPost


@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)


@admin.register(ForumThread)
class ForumThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creator',
                    'created_at', 'is_pinned', 'is_locked')
    list_filter = ('category', 'is_pinned', 'is_locked')
    search_fields = ('title',)


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'created_at', 'is_edited')
    list_filter = ('thread', 'is_edited')
    search_fields = ('content',)
