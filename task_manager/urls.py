from django.urls import path
from . import views

urlpatterns = [
    path('users/create/', views.create_user, name='create_user'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('users/', views.get_users, name='get_users'),  # Add this line for retrieving all users
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
