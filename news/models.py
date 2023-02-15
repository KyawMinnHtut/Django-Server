from django.db import models

# Create your models here.
class News(models.Model):
    # premium = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=255, blank=True)
    img = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
