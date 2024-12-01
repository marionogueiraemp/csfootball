from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Team, PlayerApplication, TransferRequest
from .serializers import TeamSerializer, PlayerApplicationSerializer, TransferRequestSerializer
from csfootball_backend.decorators import cache_response


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @cache_response()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def apply(self, request, pk=None):
        team = self.get_object()
        application = PlayerApplication.objects.create(
            player=request.user,
            team=team,
            status='PENDING'
        )
        return Response(PlayerApplicationSerializer(application).data)


class PlayerApplicationViewSet(viewsets.ModelViewSet):
    queryset = PlayerApplication.objects.all()
    serializer_class = PlayerApplicationSerializer

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        application = self.get_object()
        application.status = 'ACCEPTED'
        application.save()
        application.team.players.add(application.player)
        return Response({'status': 'accepted'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        application = self.get_object()
        application.status = 'REJECTED'
        application.save()
        return Response({'status': 'rejected'})


class TransferRequestViewSet(viewsets.ModelViewSet):
    queryset = TransferRequest.objects.all()
    serializer_class = TransferRequestSerializer

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        transfer = self.get_object()
        transfer.status = 'ACCEPTED'
        transfer.save()

        player = transfer.player
        from_team = transfer.from_team
        to_team = transfer.to_team

        from_team.players.remove(player)
        to_team.players.add(player)

        return Response({'status': 'accepted'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        transfer = self.get_object()
        transfer.status = 'REJECTED'
        transfer.save()
        return Response({'status': 'rejected'})
