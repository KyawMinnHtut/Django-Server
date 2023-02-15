from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category

class Channels(models.Model):
    title = models.CharField(max_length=25)
    img = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title  
