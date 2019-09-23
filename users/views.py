from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from .models import CustomUser
from eventFinderApp.models import Event

class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class Login(LoginView):
    template_name = 'registration/login.html'

class Logout(LogoutView):
    pass

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'account.html'
