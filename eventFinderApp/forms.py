from django import forms
from django.forms import ModelForm, DateTimeInput
from django.contrib.admin import widgets

from .models import Event

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
        'title', 
        'location', 
        'venue',  
        'start_time',
        'end_time', 
        'categories',)
        widgets = {
            'start_time': widgets.AdminSplitDateTime,
            'end_time': widgets.AdminSplitDateTime,
        }
