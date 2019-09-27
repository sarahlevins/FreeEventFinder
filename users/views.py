from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
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

class EditUserDetailView(LoginRequiredMixin, UpdateView):
    template_name = 'edit_account.html'
    form_class = CustomUserChangeForm

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('users:account', kwargs={'pk': user_id})

    def get_object(self):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, pk=user_id)
    
        
