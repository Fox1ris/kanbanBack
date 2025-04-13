from django.urls import path
from .views import ProjectListView, KanbanTaskListView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('tasks/', KanbanTaskListView.as_view(), name='tasks'),
]