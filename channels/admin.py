from django.contrib import admin
from .models import Channels

# Register your models here.
# admin.site.register(Channels)
@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title__startswith",)