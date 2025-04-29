from django.contrib import admin
from .models import Project, KanbanTask, CustomUser

admin.site.register(Project)
admin.site.register(KanbanTask)
admin.site.register(CustomUser)


