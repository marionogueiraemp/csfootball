from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ForumSection, Thread, Post
from .serializers import ForumSectionSerializer, ThreadSerializer, PostSerializer
from users.permissions import IsNewsManager  # Assuming custom permissions for News Manager

class ForumSectionViewSet(viewsets.ModelViewSet):
    queryset = ForumSection.objects.all()
    serializer_class = ForumSectionSerializer
    permission_classes = [IsAuthenticated, IsNewsManager]

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated, IsNewsManager]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsNewsManager]