from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('todolist/', views.TodoList.as_view(), name='todo_list'),
    path('todolist/<int:pk>',
         views.TodoDetail.as_view(), name='todo_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]
