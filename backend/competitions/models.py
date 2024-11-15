from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from teams.models import Team
import datetime


class Competition(models.Model):
    COMPETITION_TYPE_CHOICES = [
        ('LEAGUE', 'League'),
        ('CUP', 'Cup')
    ]
    name = models.CharField(max_length=100)
    competition_type = models.CharField(
        max_length=10, choices=COMPETITION_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_fixtures(self, start_date=None, home_and_away=False):
        if not start_date:
            start_date = datetime.date.today()

        teams = list(self.teams.all())
        if len(teams) < 2:
            return  # Exit if not enough teams to create matches

        fixtures = []
        num_teams = len(teams)
        # Number of rounds needed
        num_rounds = num_teams - 1 if num_teams % 2 == 0 else num_teams

        # Add a "bye" if the number of teams is odd
        if num_teams % 2 != 0:
            teams.append(None)

        # Generate matches for each round
        for round_num in range(num_rounds):
            round_matches = []
            for i in range(len(teams) // 2):
                team1 = teams[i]
                team2 = teams[-(i + 1)]
                if team1 and team2:  # Exclude "bye" matches
                    round_matches.append((team1, team2))

        # Rotate teams clockwise, keeping the first team in place
        teams.insert(1, teams.pop())

        # Schedule matches for the round
        round_date = start_date + datetime.timedelta(weeks=round_num)
        for team1, team2 in round_matches:
            # Create the match instance for team1 vs team2
            Match.objects.create(
                competition=self,
                team1=team1,
                team2=team2,
                date=round_date,
            )
            fixtures.append((team1, team2, round_date))

            if home_and_away:
                # Create the reverse fixture for team2 vs team1
                Match.objects.create(
                    competition=self,
                    team1=team2,
                    team2=team1,
                    # Schedule midweek
                    date=round_date + datetime.timedelta(days=3),
                )
                fixtures.append((team2, team1, round_date +
                                datetime.timedelta(days=3)))

        return fixtures

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = get_channel_layer()
        group_name = f"match_{self.id}"
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send_match_update",
                "update": {
                    "id": self.id,
                    "team1": self.team1.name,
                    "team2": self.team2.name,
                    "team1_score": self.team1_score,
                    "team2_score": self.team2_score,
                },
            },
        )

    def __str__(self):
        return f"{self.name} ({self.get_competition_type_display()})"

# @receiver(post_save, sender=Competition)
# def create_fixtures_on_competition_creation(sender, instance, created, **kwargs):
    """
    Automatically generate fixtures when a new competition is created.
    """
    # if created and instance.competition_type == 'LEAGUE':
    # Set the start date and whether to include home and away matches
    # start_date = datetime.date.today()
    # home_and_away = True  # Set to False if only single matches are desired

    # Generate and save fixtures
    # instance.generate_fixtures(start_date=start_date, home_and_away=home_and_away)


class Match(models.Model):
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name="matches")
    team1 = models.ForeignKey(
        'teams.Team', on_delete=models.CASCADE, related_name="home_matches")
    team2 = models.ForeignKey(
        'teams.Team', on_delete=models.CASCADE, related_name="away_matches")
    date = models.DateTimeField()
    team1_score = models.IntegerField(null=True, blank=True)
    team2_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date.strftime('%Y-%m-%d %H:%M')}"
        return f"{self.team1} vs {self.team2} - {self.date.strftime('%Y-%m-%d %H:%M')}"


class PlayerStats(models.Model):
    match = models.ForeignKey(
        'competitions.Match', on_delete=models.CASCADE, related_name="player_stats")
    player = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.username} - {self.match} Stats"
