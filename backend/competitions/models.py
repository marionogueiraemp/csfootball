from django.db import models
from users.models import CustomUser
from teams.models import Team
from csfootball_backend.decorators import cache_model


@cache_model()
class Competition(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team, related_name='competitions')
    start_date = models.DateField()
    end_date = models.DateField()

    COMPETITION_TYPES = [
        ('LEAGUE', 'League'),
        ('CUP', 'Cup'),
        ('TOURNAMENT', 'Tournament')
    ]
    competition_type = models.CharField(
        max_length=20, choices=COMPETITION_TYPES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


@cache_model()
class Match(models.Model):
    competition = models.ForeignKey(
        Competition, related_name='matches', on_delete=models.CASCADE)
    home_team = models.ForeignKey(
        Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(
        Team, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    match_date = models.DateTimeField()

    MATCH_STATUS = [
        ('SCHEDULED', 'Scheduled'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]
    status = models.CharField(
        max_length=20, choices=MATCH_STATUS, default='SCHEDULED')


class PlayerStats(models.Model):
    player = models.ForeignKey(
        CustomUser, related_name='player_stats', on_delete=models.CASCADE)
    match = models.ForeignKey(
        Match, related_name='player_stats', on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField
