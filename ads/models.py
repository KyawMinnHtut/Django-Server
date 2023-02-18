from django.db import models

# Create your models here.

SCREENS = (
    ("live", "live"),
    ("highlights", "highlights"),
    ("channels", "channels"),
)

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
    screen = models.CharField(max_length=15, choices = SCREENS, default="live")

    def __str__(self):
        return self.link + " ("+self.screen+")" 

class TextAds(models.Model):
    text = models.CharField(max_length=255)
    show = models.BooleanField()
    link = models.CharField(max_length=255)
    messenger = models.CharField(max_length=10)

    def __str__(self):
        return self.link   
