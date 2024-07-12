from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    data = {'user' : request.user}
    return render(request, 'registration/profile.html', context=data)