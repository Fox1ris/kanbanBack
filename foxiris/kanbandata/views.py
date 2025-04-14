from rest_framework.response import Response

from .models import Project, KanbanTask
from .serializers import ProjectSerializer, KanbanTaskSerializer
from rest_framework import generics, viewsets

class ProjectListView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class KanbanTaskListView(viewsets.ModelViewSet):
    queryset = KanbanTask.objects.all()
    serializer_class = KanbanTaskSerializer

