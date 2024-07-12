from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # представления поста
    path('', views.tasks_list, name='tasks_list'),
    path('create/', views.create),
]