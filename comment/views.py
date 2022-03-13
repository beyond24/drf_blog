from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from comment.models import Comment
from .permisssions import IsOwnerOrReadOnly
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)