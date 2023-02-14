from django.contrib import admin
from .models import Ads, ImageAds, TextAds

# Register your models here.
# admin.site.register(Channels)
@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ("img", "link", "messenger")

@admin.register(ImageAds)
class ImageAdsAdmin(admin.ModelAdmin):
    list_display = ("img", "link", "messenger")

@admin.register(TextAds)
class TextAdsAdmin(admin.ModelAdmin):
    list_display = ("text", "link", "messenger", "show")