from django.contrib import admin
from .models import News

# Register your models here.
# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "body")
    search_fields = ("title__startswith",)