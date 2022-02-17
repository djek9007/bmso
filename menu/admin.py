from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from menu.models import Menu


class MenuAdmin(MPTTModelAdmin):
    save_on_top = True
    list_display_links = ("name",)
    list_display = ['name', 'parent','slug', 'published']
    prepopulated_fields = {'slug': ('name',)}
    # list_editable = ['description',]
    mptt_level_indent = 20

admin.site.register(Menu, MenuAdmin)