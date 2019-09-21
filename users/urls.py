from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginView.as_view, name = 'login'),
    path('logout/', views.LogoutView.as_view, name = 'logout'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='account'),
]