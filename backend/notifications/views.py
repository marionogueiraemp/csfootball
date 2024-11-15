from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from django.urls import reverse
from django.db.models import F, Case, When, Value, CharField


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        queryset = Notification.objects.filter(user=self.request.user)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def perform_update(self, serializer):
        # Mark notification as read when updated
        serializer.save(is_read=True)
