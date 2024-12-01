from django.db import models
from users.models import CustomUser
from csfootball_backend.decorators import cache_model


@cache_model()
class ForumCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Forum Categories'
        ordering = ['order']

    def __str__(self):
        return self.name


@cache_model()
class ForumThread(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        ForumCategory, on_delete=models.CASCADE, related_name='threads')
    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='forum_threads')
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.title


@cache_model()
class ForumPost(models.Model):
    thread = models.ForeignKey(
        ForumThread, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='forum_posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)

    def __str__(self):
        return f"Post by {self.author.username} in {self.thread.title}"
