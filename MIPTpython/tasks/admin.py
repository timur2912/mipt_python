from django.contrib import admin
from .models import Task, Project1

admin.site.register(Task)



@admin.register(Project1)
class Project1Admin(admin.ModelAdmin):
    list_display = ['user_name', 'link', 'score', 'status', ]