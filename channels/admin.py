from django.contrib import admin
from .models import Channels, Category

# Register your models here.
# admin.site.register(Channels)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "category")
    search_fields = ("title__startswith",)
    list_filter = ("category",)
