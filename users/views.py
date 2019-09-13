from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from .models import CustomUser

class Register(generic.CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/register.html'

class Login(LoginView):
  template_name = 'registration/login.html'

class Logout(LogoutView):
  pass

class UserDetailView(generic.DetailView):
  model = CustomUser
  template_name = 'account.html'
