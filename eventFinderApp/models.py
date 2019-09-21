from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import CustomUser

class Event(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null = "True")
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    venue = models.CharField(max_length=200, null="True")
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category')

    def get_absolute_url(self):
        return reverse("eventFinderApp:event", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
