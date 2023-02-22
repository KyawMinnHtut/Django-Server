from django.contrib import admin
from .models import Category, Movie, Link

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Movie)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "quality", "link")
    search_fields = ("name__startswith", )
    list_filter = ("quality",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("movieName", "category", "premium")
    search_fields = ("movieName__startswith",)
    list_filter = ("category","premium")
    # list_filter = ("premium",)
