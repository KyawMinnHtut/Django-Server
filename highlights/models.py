from django.db import models


# Create your models here.
class HighLightLink(models.Model):
    # live = models.ForeignKey(Live, on_delete=models.SET_NULL, blank=True, null=True)
    video_type = models.CharField(max_length=15, null=True)
    highlightlink = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.highlightlink

class HighLight(models.Model):
    premium = models.BooleanField(default=False)
    league = models.CharField(max_length=50, null=True)
    date = models.DateField(blank=True)
    result = models.CharField(max_length=50, null=True)
    himg = models.CharField(max_length=100, null=True)
    aimg = models.CharField(max_length=100, null=True)
    teams = models.CharField(max_length=50, null=True)
    hteam = models.CharField(max_length=50, null=True)
    ateam = models.CharField(max_length=50, null=True)
    link = models.ManyToManyField(HighLightLink, blank=True)

    def __str__(self):
        return self.teams