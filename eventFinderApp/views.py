from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            form.save_m2m()
            return redirect('/event-finder/')
    else:
        form = PostForm()
    return render(request, 'eventFinderApp/event_submit.html', {'form': form})

def account(request):
    return render(request, 'eventFinderApp/account.html')