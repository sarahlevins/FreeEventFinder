
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Event
from .forms import NewEventForm


class IndexView(ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class EventView(DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


class CreateEventView(LoginRequiredMixin, CreateView):
    template_name = 'eventFinderApp/event_submit.html'
    form_class = NewEventForm
    login_url = '/users/login/'

    def form_valid(self, form):
        form.instance.host = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)

class EditEventView(LoginRequiredMixin, UpdateView):
    template_name = 'eventFinderApp/event_edit.html'
    form_class = NewEventForm

    def get_object(self):
        event_id = self.kwargs.get('pk')
        return get_object_or_404(Event, pk=event_id, host=self.request.user)






