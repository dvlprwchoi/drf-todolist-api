from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    task = models.TextField()
    author = models.ForeignKey(
        'users.User', related_name='todolist', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'users.User', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
