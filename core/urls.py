from django.urls import path
from .views import JobListCreateAPI, UserListCreateAPI

urlpatterns = [
    path('jobs/', JobListCreateAPI.as_view(), name='job-list-create'),
    path('users/', UserListCreateAPI.as_view(), name='user-list-create'),
]