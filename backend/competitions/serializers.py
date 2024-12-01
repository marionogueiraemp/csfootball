from rest_framework import serializers
from .models import Competition, Match, PlayerStats
from teams.models import Team


class PlayerStatsSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(
        source='player.username', read_only=True)

    class Meta:
        model = PlayerStats
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    home_team_name = serializers.CharField(
        source='home_team.name', read_only=True)
    away_team_name = serializers.CharField(
        source='away_team.name', read_only=True)
    player_stats = PlayerStatsSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    team_count = serializers.SerializerMethodField()
    matches = MatchSerializer(many=True, read_only=True)

    class Meta:
        model = Competition
        fields = ['id', 'name', 'teams', 'start_date',
                  'end_date', 'matches', 'team_count']

    def get_team_count(self, obj):
        return obj.teams.count()
