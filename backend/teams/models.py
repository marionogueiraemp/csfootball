from django.db import models
from users.models import CustomUser
from csfootball_backend.decorators import cache_model


@cache_model()
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='owned_team')
    players = models.ManyToManyField(CustomUser, related_name='teams')
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Team Statistics
    matches_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    # Team Status
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-points', '-goals_scored']


class PlayerApplication(models.Model):
    player = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='applications')
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected')
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} -> {self.team.name}"


class TransferRequest(models.Model):
    player = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='transfers')
    from_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='transfers_out')
    to_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='transfers_in')
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected')
    ], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username}: {self.from_team.name} -> {self.to_team.name}"
