from django.urls import path
from .views import (
    BaseView,
    TaskListView,
    TaskListByIdView,
    TaskListByIdTitleView,
    TaskListUndoneByIdTitleView,
    TaskListDoneByIdTitleView,
    TaskListDoneIdsView,
    TaskListUndoneIdsView,
    TaskCreateView,
    TaskUpdateView, 
    TaskDeleteView
)

app_name = 'pendings'

urlpatterns = [
    path('base/', BaseView.as_view(), name="base"),
    path('tasks/', TaskListView.as_view(), name="task_list"),
    path('tasks/just/id/', TaskListByIdView.as_view(), name="task_just_id"),
    path('tasks/just/id/title/', TaskListByIdTitleView.as_view(), name="task_just_id_title"),
    path('tasks/undone/id/title/', TaskListUndoneByIdTitleView.as_view(), name="task_undone_id_title"),
    path('tasks/done/id/title/', TaskListDoneByIdTitleView.as_view(), name="task_done_id_title"),
    path('tasks/done/ids/', TaskListDoneIdsView.as_view(), name="task_done_ids"),
    path('tasks/undone/ids/', TaskListUndoneIdsView.as_view(), name="task_undone_ids"),
    path('crud/insert/', TaskCreateView.as_view(), name="crud_insert"),
    path('crud/update/<int:pk>/', TaskUpdateView.as_view(), name='crud_update'),
    path('crud/delete/<int:pk>/', TaskDeleteView.as_view(), name='crud_delete'),
]
