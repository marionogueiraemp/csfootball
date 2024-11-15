from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    ROLE_CHOICES = [
        ("ADMIN", "Administrator"),
        ("LEAGUE_MANAGER", "League Manager"),
        ("NEWS_MANAGER", "News Manager"),
        ("TEAM_OWNER", "Team Owner"),
        ("PLAYER", "Player"),
    ]
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="PLAYER")

    def __str__(self):
        return self.username

    # Add related_name attributes to avoid conflicts with Django's default User model
    groups = models.ManyToManyField(
        "auth.Group",
        # Avoid conflict by renaming the reverse relationship
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        # Avoid conflict by renaming the reverse relationship
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
