from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectListView, KanbanTaskListView

router = DefaultRouter()
router.register(r'projects', ProjectListView)
router.register(r'tasks', KanbanTaskListView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]