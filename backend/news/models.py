from django.db import models
from django.utils import timezone

class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Interview(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class HistoricalEvent(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.event_title
