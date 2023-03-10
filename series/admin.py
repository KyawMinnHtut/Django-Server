from django.contrib import admin
from .models import Series, Part, Link, Category

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Movie)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ("sname", "category", "premium")
    search_fields = ("sname__startswith",)
    list_filter = ("category","premium")

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ("part", )
    # list_filter = ("premium",)
    # search_fields = ("sname__startswith",)

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("name", "quality", "link")
    search_fields = ("name__startswith", )
    list_filter = ("quality",)
