from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.
class CustomUser(AbstractUser):
    premium_date = models.DateField(default=now, blank=True)
