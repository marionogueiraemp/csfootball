from rest_framework import serializers
from .models import Competition, Match, PlayerStats

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'name', 'competition_type', 'created_at']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'competition', 'team1', 'team2', 'date', 'team1_score', 'team2_score']

class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        fields = ['id', 'match', 'player', 'goals', 'assists', 'yellow_cards', 'red_cards']
