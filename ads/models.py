from django.db import models

# Create your models here.
class Ads(models.Model):
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    messenger = models.CharField(max_length=10)

    def __str__(self):
        return self.link
    
class ImageAds(models.Model):
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    messenger = models.CharField(max_length=10)

    def __str__(self):
        return self.link 

class TextAds(models.Model):
    text = models.CharField(max_length=255)
    show = models.BooleanField()
    link = models.CharField(max_length=255)
    messenger = models.CharField(max_length=10)

    def __str__(self):
        return self.link   
