from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectListView, KanbanTaskListView, RegisterViewSet, LoginViewSet, UserListView

router = DefaultRouter()
router.register(r'projects', ProjectListView)
router.register(r'tasks', KanbanTaskListView, basename='task')
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'users', UserListView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]