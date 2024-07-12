from django.urls import path
from . import views



urlpatterns = [
    # представления поста
    path('', views.scores_list, name='scores_list'),
]