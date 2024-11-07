# core/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('league_manager', 'League Manager'),
        ('news_manager', 'News Manager'),
        ('team_owner', 'Team Owner'),
        ('player', 'Player'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
        # Add unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_teams")
    created_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='team_avatars/', null=True, blank=True)

class Competition(models.Model):
    COMPETITION_TYPES = [
        ('league', 'League'),
        ('cup', 'Cup'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=COMPETITION_TYPES)
    status = models.CharField(max_length=20, default='upcoming')
    teams = models.ManyToManyField(Team, related_name="competitions")

class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="matches")
    date = models.DateTimeField()
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team_a")
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="matches_as_team_b")
    score_a = models.PositiveIntegerField(default=0)
    score_b = models.PositiveIntegerField(default=0)

class PlayerStatistics(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'player'})
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="player_statistics")
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)

class TransferWindow(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_transfers = models.PositiveIntegerField()
