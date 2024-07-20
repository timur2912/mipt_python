from django.urls import path
from .views import SignUpView
from .views import SignUpView, profile, perform_login

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', profile, name='users-profile'),
    path('perform_login', perform_login, name='perform_login')
]