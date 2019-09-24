from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import url
from . import views

app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    path('event_submit/', views.CreateEventView.as_view(), name='event_submit'),
    path('event_edit/<int:pk>/', views.EditEventView.as_view(), name='event_edit'),
    path('event_filter', views.FilterView.as_view(), name='event_filter')]