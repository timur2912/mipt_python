from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    data = {'user' : request.user, 'profile' : Profile.objects.get(user=request.user)}
    return render(request, 'registration/profile.html', context=data)


def render_login(request):
    return render(request, 'login.html')

def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username,
                                password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect('profile/')
        else:
            messages.error(request, "Неправильные имя пользователя или пароль")
            return HttpResponseRedirect('login/')