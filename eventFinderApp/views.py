from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from .models import Event, Category
from .forms import PostForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

def event_submit(request):
    form = PostForm()
    return render(request, 'eventFinderApp/event_submit.html', {'form': form})

def account(request):
    return render(request, 'eventFinderApp/account.html')