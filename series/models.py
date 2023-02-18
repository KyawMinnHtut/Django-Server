from django.db import models


# Create your models here.

QUALITY = (
    ("SD", "SD"),
    ("HD", "HD"),
    ("FHD", "FHD"),
)

class Link(models.Model):
    name = models.CharField(max_length=25)
    quality = models.CharField(max_length=5, choices = QUALITY, default="SD")
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.name + "  (" +self.quality +")"

class Part(models.Model):
    # live = models.ForeignKey(Live, on_delete=models.SET_NULL, blank=True, null=True)
    sname = models.CharField(max_length=50, null=True, blank=True)
    part = models.CharField(max_length=5, null=True)
    # downloadLink = models.CharField(max_length=15, null=True)
    playLink = models.ManyToManyField(Link, blank=True)
    def __str__(self):
        return self.sname + " ( Part "+self.part+" )"
        
class Category(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category

class Series(models.Model):
    premium = models.BooleanField(default=False)
    sname = models.CharField(max_length=50, null=True)
    popular = models.BooleanField(default=False)
    year = models.CharField(max_length=10, blank=True)
    img = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    link = models.ManyToManyField(Part, blank=True)
    def __str__(self):
        return self.sname
