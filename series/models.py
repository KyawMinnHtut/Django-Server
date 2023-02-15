from django.db import models


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=25)
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Part(models.Model):
    # live = models.ForeignKey(Live, on_delete=models.SET_NULL, blank=True, null=True)
    part = models.CharField(max_length=5, null=True)
    # downloadLink = models.CharField(max_length=15, null=True)
    playLink = models.ManyToManyField(Link, blank=True)
    def __str__(self):
        return self.part

class Series(models.Model):
    premium = models.BooleanField(default=False)
    sname = models.CharField(max_length=50, null=True)
    img = models.CharField(max_length=100, null=True)
    desc = models.TextField(blank=True, null=True)
    link = models.ManyToManyField(Part)
    def __str__(self):
        return self.sname
