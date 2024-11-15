from django.contrib import admin
from .models import NewsPost, Interview, HistoricalEvent

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

@admin.register(HistoricalEvent)
class HistoricalEventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_date')