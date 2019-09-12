from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.views.generic import CreateView
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

# def event_submit(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.save()
#             form.save_m2m()
#             return redirect('/event-finder/')
#     else:
#         form = PostForm()
#     return render(request, 'eventFinderApp/event_submit.html', {'form': form})

# class FormView(View):
#     form_class = NewEventForm
#     initial = {'key': 'value'}
#     template_name: 'event_submit.html'

#     def get(self):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.save()
#             form.save_m2m()
#             return redirect('/event-finder/')
#         return render(request, self.template_name, {'form': form})

class CreateEventView(CreateView):
    template_name = 'eventFinderApp/event_submit.html'
    form_class = NewEventForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

def account(request):
    return render(request, 'eventFinderApp/account.html')