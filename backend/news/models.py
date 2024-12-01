from django.db import models
from users.models import CustomUser
from csfootball_backend.decorators import cache_model


@cache_model()
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ARTICLE_TYPES = [
        ('NEWS', 'News'),
        ('INTERVIEW', 'Interview'),
        ('BLOG', 'Blog Post')
    ]
    article_type = models.CharField(max_length=10, choices=ARTICLE_TYPES)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
