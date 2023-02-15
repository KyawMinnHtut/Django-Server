from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category
    
class Link(models.Model):
    name = models.CharField(max_length=25)
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Movie(models.Model):
    premium = models.BooleanField(default=False)
    movieName = models.CharField(max_length=50)
    popular = models.BooleanField(default=False)
    year = models.CharField(max_length=10)
    desc = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=100)
    downloadLink = models.ManyToManyField(Link, blank=True)
    # playLink = models.ManyToManyField(Link, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.movieName
