from .models import Project, KanbanTask
from .serializers import ProjectSerializer, KanbanTaskSerializer
from rest_framework import generics, viewsets

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class KanbanTaskListView(generics.ListAPIView):
    queryset = KanbanTask.objects.all()
    serializer_class = KanbanTaskSerializer
