from rest_framework import viewsets, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Competition, Match, PlayerStats
from .serializers import CompetitionSerializer, MatchSerializer, PlayerStatsSerializer
from users.permissions import IsLeagueManager, IsTeamOwner


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated, IsLeagueManager]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated, IsLeagueManager])
    def apply_team(self, request, pk=None):
        competition = self.get_object()
        team_id = request.data.get('team_id')
        if team_id:
            team = Team.objects.get(id=team_id)
            competition.teams.add(team)
            return Response({'status': 'team applied successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Team ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated, IsTeamOwner])
    def apply_team(self, request, pk=None):
        competition = self.get_object()
        team_id = request.data.get('team_id')
        team = Team.objects.get(id=team_id, owner=request.user)
        competition.teams.add(team)
        return Response({'status': 'application submitted'})

    @action(detail=True, methods=['post'], permission_classes=[IsLeagueManager])
    def generate_fixtures(self, request, pk=None):
        competition = self.get_object()
        competition.generate_fixtures()  # Assuming this method exists in the model
        return Response({"message": "Fixtures generated successfully."})

    @action(detail=True, methods=['patch'], permission_classes=[IsLeagueManager])
    def update_scores(self, request, pk=None):
        match = self.get_object()
        match.team1_score = request.data.get('team1_score')
        match.team2_score = request.data.get('team2_score')
        match.save()
        return Response({"message": "Match updated successfully."})


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated, IsLeagueManager]


class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer
    permission_classes = [IsAuthenticated, IsLeagueManager]
