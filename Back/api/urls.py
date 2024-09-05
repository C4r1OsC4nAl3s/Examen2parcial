from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('tasks/list/', views.TaskList.as_view(), name='task-list'),
    path('tasks/done/', views.TasksListDone.as_view(), name='task-list-done'),
    path('tasks/undone/', views.TasksListUndone.as_view(), name='task-list-undone'),
    path('tasks/detail/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
