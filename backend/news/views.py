from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import NewsPost, Interview, HistoricalEvent
from .serializers import NewsPostSerializer, InterviewSerializer, HistoricalEventSerializer
from users.permissions import IsNewsManager


class NewsPostViewSet(viewsets.ModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer
    permission_classes = [permissions.IsAuthenticated, IsNewsManager]


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsNewsManager]


class HistoricalEventViewSet(viewsets.ModelViewSet):
    queryset = HistoricalEvent.objects.all().order_by(
        '-event_date')  # Updated to use event_date
    serializer_class = HistoricalEventSerializer
    permission_classes = [permissions.IsAuthenticated, IsNewsManager]
