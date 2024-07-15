from django.contrib import admin
from .models import Task, Project1
from django.utils.html import format_html


@admin.register(Task)
class Task1Admin(admin.ModelAdmin):
    list_display = ['task_type', 'publish', ]
    list_editable = ['publish',]


@admin.register(Project1)
class Project1Admin(admin.ModelAdmin):
    @admin.display(description="project")
    def show_project(self, obj):
        return format_html("<a href='{url}'>Ссылка на проект</a>", url=obj.link)

    list_display = ['user_name', 'checker', 'show_project', 'score', 'status', ]
    list_editable = ('status', 'score')
    list_filter = ['checker',]
    search_fields = ['user_name',]