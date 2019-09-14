from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from .models import Event, Category
from .forms import NewEventForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

class CreateEventView(LoginRequiredMixin, CreateView):
    template_name = 'eventFinderApp/event_submit.html'
    form_class = NewEventForm

    def form_valid(self, form):
        form.instance.host = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)

class EditEventView(UpdateView):
    template_name = 'eventFinderApp/event_edit.html'
    form_class = NewEventForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_object(self):
        event_id = self.kwargs.get('pk')
        return get_object_or_404(Event, pk=event_id)
