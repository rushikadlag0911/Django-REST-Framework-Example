from django.urls import path
from .views import create_task, get_tasks

urlpatterns = [
    path('tasks/', get_tasks, name='tasks'),
    path('create_task/', create_task, name='create_task')
]