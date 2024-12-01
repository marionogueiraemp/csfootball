from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Competition, Match, PlayerStats
from .serializers import CompetitionSerializer, MatchSerializer, PlayerStatsSerializer
from csfootball_backend.permissions import IsLeagueManager
from csfootball_backend.decorators import cache_response


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Competition.objects.all()

    @cache_response()
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @cache_response()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def standings(self, request, pk=None):
        competition = self.get_object()
        teams = competition.teams.all()
        standings = []

        for team in teams:
            standings.append({
                'team': team.name,
                'matches_played': team.matches_played,
                'wins': team.wins,
                'draws': team.draws,
                'losses': team.losses,
                'goals_scored': team.goals_scored,
                'goals_conceded': team.goals_conceded,
                'points': team.points
            })

        return Response(sorted(standings, key=lambda x: (-x['points'], -x['goals_scored'])))


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        match_id = self.kwargs.get('pk')
        if match_id:
            return Match.objects.filter(id=match_id)
        return Match.objects.all()

    @action(detail=True, methods=['post'])
    def record_result(self, request, pk=None):
        match = self.get_object()
        home_score = request.data.get('home_score')
        away_score = request.data.get('away_score')

        if home_score is None or away_score is None:
            return Response({'error': 'Scores required'}, status=status.HTTP_400_BAD_REQUEST)

        # Update match result and team statistics
        match.home_team.update_stats(home_score, away_score, True)
        match.away_team.update_stats(away_score, home_score, False)

        return Response({'status': 'result recorded'})

    @action(detail=True, methods=['get'])
    def player_stats(self, request, pk=None):
        match = self.get_object()
        player_stats = PlayerStats.objects.filter(match=match)
        serializer = PlayerStatsSerializer(player_stats, many=True)
        return Response(serializer.data)


class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer
    # Changed from IsLeagueManager
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        match_id = self.request.query_params.get('match')
        if match_id:
            return PlayerStats.objects.filter(match_id=match_id)
        return PlayerStats.objects.all()
