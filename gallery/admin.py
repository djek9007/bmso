from django.contrib import admin

# Register your models here.
from gallery.models import Year, PhotoItem, Albom



class PhotoItemInline(admin.TabularInline):
    model = PhotoItem
    extra = 10

class AlbomAdmin(admin.ModelAdmin):
    list_display = ['name', 'year',]
    inlines = [PhotoItemInline]

admin.site.register(Albom, AlbomAdmin)
admin.site.register(Year)