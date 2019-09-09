from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from .models import Event
from .forms import NameForm


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()

class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    
    return render(request, 'name.html', {'form': form})

def account(request):
    return render(request, 'eventFinderApp/account.html')