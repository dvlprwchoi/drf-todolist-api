from rest_framework import generics  # <- import generics
from .models import Todo, Comment  # <- don't forget your models
from .serializers import TodoSerializer, CommentSerializer  # <- or serializers
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # check if user is authenticated before letting them post
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # overwrite the underlying perform_create method to save the owner as the user making the request
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # check if user is authenticated before letting them post
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
