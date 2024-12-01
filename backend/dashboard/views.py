from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdministrator, IsLeagueManager, IsNewsManager, IsTeamOwner, IsPlayer
from competitions.models import Competition
from news.models import NewsPost, HistoricalEvent, Interview
from teams.models import Team, PlayerApplication, TransferRequest
from users.models import CustomUser
from notifications.models import Notification


# Administrator Dashboard
class AdminDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsAdministrator]

    def get(self, request):
        total_users = CustomUser.objects.count()
        total_teams = Team.objects.count()
        total_competitions = Competition.objects.count()
        return Response({
            "total_users": total_users,
            "total_teams": total_teams,
            "total_competitions": total_competitions,
        })


# League Manager Dashboard
class LeagueManagerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsLeagueManager]

    def get(self, request):
        competitions = Competition.objects.filter(league_manager=request.user)
        applications = PlayerApplication.objects.filter(
            team__competitions__league_manager=request.user, status='PENDING')
        return Response({
            "competitions": competitions.values("name", "competition_type", "created_at"),
            "pending_applications": applications.count(),
        })


# News Manager Dashboard
class NewsManagerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsNewsManager]

    def get(self, request):
        news_posts = NewsPost.objects.filter(author=request.user).count()
        interviews = Interview.objects.filter(author=request.user).count()
        historical_events = HistoricalEvent.objects.count()
        return Response({
            "news_posts": news_posts,
            "interviews": interviews,
            "historical_events": historical_events,
        })


# Team Owner Dashboard
class TeamOwnerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsTeamOwner]

    def get(self, request):
        teams = Team.objects.filter(owner=request.user).values("name", "logo")
        transfer_requests = TransferRequest.objects.filter(
            to_team__owner=request.user, status='PENDING').count()
        return Response({
            "teams": teams,
            "pending_transfer_requests": transfer_requests,
        })


# Player Dashboard
class PlayerDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsPlayer]

    def get(self, request):
        team_membership = Team.objects.filter(
            players=request.user).values("name", "logo")
        notifications = Notification.objects.filter(
            user=request.user, is_read=False).count()
        return Response({
            "team_membership": team_membership,
            "unread_notifications": notifications,
        })
