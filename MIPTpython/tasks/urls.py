from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    # представления поста
    path('', views.tasks_list, name='tasks_list'),
    path('create_1/', views.create_1),
    path('update_field_1/', views.update_field_1),

    path('create_2/', views.create_2),
    path('update_field_2/', views.update_field_2),

    path('create_lab/', views.create_lab),
    path('update_field_lab/', views.update_field_lab),
]