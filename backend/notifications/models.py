from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Notification(models.Model):
    CATEGORY_CHOICES = [
        ('TRANSFER', 'Transfer'),
        ('MATCH', 'Match'),
        ('GENERAL', 'General'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"
