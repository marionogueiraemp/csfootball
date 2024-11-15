from django.contrib import admin
from .models import ForumSection, Thread, Post

@admin.register(ForumSection)
class ForumSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'created_by', 'created_at')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('thread', 'created_by', 'created_at', 'content')