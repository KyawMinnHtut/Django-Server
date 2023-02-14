from django.contrib import admin

from .models import HighLight, HighLightLink

# Register your models here.
# admin.site.register(HighLight)
# admin.site.register(HighLightLink)

@admin.register(HighLight)
class HighLightAdmin(admin.ModelAdmin):
    list_display = ("teams", "result", "date","premium")
    list_filter = ("date",)
    search_fields = ("teams__startswith",)

@admin.register(HighLightLink)
class HighLightLinkAdmin(admin.ModelAdmin):
    list_display = ("video_type", "highlightlink")