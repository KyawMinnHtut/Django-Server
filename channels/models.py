from django.db import models

# Create your models here.
class Channels(models.Model):
    title = models.CharField(max_length=25)
    img = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.title  
