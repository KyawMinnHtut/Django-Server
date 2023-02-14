from django.contrib import admin
from django.db import models

from myapp.models import LiveLinks, Live

# Register your models here.
# admin.site.register(Live)
# admin.site.register(LiveLinks)

# class LinksAdmin(admin.TabularInline):
#     model = LiveLinks
#     extra = 1

@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):
    list_display = ("teams", "date", "time", "status","premium")
    # inlines = [LinksAdmin, ]
    list_filter = ("date", "premium")
    search_fields = ("teams__startswith", )

@admin.register(LiveLinks)
class LiveLinksAdmin(admin.ModelAdmin):
    list_display = ("video_type", "livelink")