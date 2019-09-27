from django import forms
from .models import Event, Category
import django_filters

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget = forms.CheckboxSelectMultiple)

    class Meta:
        model = Event
        fields = ['title', 'location', 'categories']
        

            # 'title': ['icontains'],
            # 'location': ['icontains'],
            # 'categories': ['exact']