from django.db import models
from django.utils import timezone
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=15000)
    date = models.DateTimeField(default=timezone.now)
    room = models.CharField(max_length=10000)
    user = models.CharField(max_length=10000)