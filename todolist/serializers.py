from rest_framework import serializers
from .models import Todo, Comment


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    todo_url = serializers.ModelSerializer.serializer_url_field(
        view_name='todo_detail')
    owner = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Todo
        fields = ('id', 'title', 'place', 'task', 'created', 'comments',
                  'todo_url', 'author',)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    todo = serializers.HyperlinkedRelatedField(
        view_name='todo_detail', read_only=True)

    todo_id = serializers.PrimaryKeyRelatedField(
        queryset=Todo.objects.all(), source='todo')

    todo_title = serializers.SlugRelatedField(
        queryset=Todo.objects.all(), slug_field='title', source='todo')

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'todo', 'todo_id', 'title',
                  'body', 'created', 'todo_title', 'author')
