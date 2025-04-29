from django.contrib.auth import get_user_model, authenticate
from knox.serializers import UserSerializer
from rest_framework.response import Response
from .models import Project, KanbanTask, CustomUser
from .serializers import ProjectSerializer, KanbanTaskSerializer, RegisterSerializer, LoginSerializer
from rest_framework import viewsets, permissions, status
from knox.models import AuthToken

User = get_user_model()

class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                _, token = AuthToken.objects.create(user)
                return Response({"user": self.serializer_class(user).data, "token": token})
            else:
                return Response({"error": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class KanbanTaskListView(viewsets.ModelViewSet):
    queryset = KanbanTask.objects.all()
    serializer_class = KanbanTaskSerializer

class UserListView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer




