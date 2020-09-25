from django.db import models
from django.db.models import Model
from PIL import Image
from signup.models import User

# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=50, blank=False, default='')
    speaker_name = models.CharField(max_length=50, blank=False, default='')
    topic = models.CharField(max_length=250, blank=False, default='')
    time_scheduled = (
        ('morning', 'Morning'),
        ('midmorning', 'Midmorning'),
        ('afternoon', 'Afternoon')
    )
    schedule = models.CharField(max_length=25, choices=time_scheduled)
    room_capacity = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=250, blank=False, default='')
    date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to = 'media/', null=True, blank=True)


def _str_(self):
        return self.title

                   
class Meta:
        ordering = ('id',)
