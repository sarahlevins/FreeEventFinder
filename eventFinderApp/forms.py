from django import forms
from django.forms import ModelForm, DateTimeInput

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
        'description', 
        'categories',)
