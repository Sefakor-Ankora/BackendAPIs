from django.db import models
from signup.models import User
from events.models import Events


# Create your models here.

class Register(models.Model):
    username =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=50, blank=False, default='')
    address = models.CharField(max_length=50, blank=False, default='')
    city = models.CharField(max_length=250, blank=False, default='')
    phone_number = models.CharField(max_length=250, blank=False, default='')

    
    
   
   
def _str_(self):
        return self.name

                   
class Meta:
        ordering = ('id',)
