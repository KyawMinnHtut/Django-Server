from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils.timezone import now
#from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    premium_date = models.DateField(default=now, blank=True)
    
    #objects = CustomUserManager()
    
    def __str__(self):
        return self.username
