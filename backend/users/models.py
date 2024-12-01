from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_player = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    # Email verification
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=100, blank=True)

    # Steam integration
    steam_id = models.CharField(max_length=100, blank=True)
    steam_profile_url = models.URLField(blank=True)

    # Player statistics
    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)

    ROLE_CHOICES = [
        ("ADMIN", "Administrator"),
        ("LEAGUE_MANAGER", "League Manager"),
        ("NEWS_MANAGER", "News Manager"),
        ("TEAM_OWNER", "Team Owner"),
        ("PLAYER", "Player"),
    ]
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default="PLAYER")

    # Team ownership relationship will be handled by a foreign key from Team model

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
