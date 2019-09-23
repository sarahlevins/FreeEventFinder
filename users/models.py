from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length=50, default='')
  last_name = models.CharField(max_length=50, default='')
  def __str__(self):
    return self.username



