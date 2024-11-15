from rest_framework import viewsets, permissions
from .models import Team, PlayerApplication, TransferRequest
from .serializers import TeamSerializer, PlayerApplicationSerializer, TransferRequestSerializer
from users.permissions import IsTeamOwner
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeamOwner]

    def get_queryset(self):
        return Team.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        if Team.objects.filter(owner=self.request.user).exists():
            raise ValidationError(
                "You already own a team and cannot create another.")
        serializer.save(owner=self.request.user)

    def retrieve(self, request, pk=None):
        team = self.get_object()
        players = team.players.annotate(
            goals=models.Sum('matchstats__goals'),
            assists=models.Sum('matchstats__assists'),
            yellow_cards=models.Sum('matchstats__yellow_cards'),
            red_cards=models.Sum('matchstats__red_cards'),
        )
        transfers = team.transfers.all()

        return Response({
            "team": TeamSerializer(team).data,
            "players": players.values("id", "username", "goals", "assists", "yellow_cards", "red_cards"),
            "transfers": TransferSerializer(transfers, many=True).data,
        })


class PlayerApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeamOwner]

    def get_queryset(self):
        return PlayerApplication.objects.filter(team__owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)


class TransferRequestViewSet(viewsets.ModelViewSet):
    serializer_class = TransferRequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsTeamOwner]

    def get_queryset(self):
        return TransferRequest.objects.filter(to_team__owner=self.request.user)
