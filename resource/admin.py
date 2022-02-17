from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from resource.models import Resource, CategoryResource


class CategoryResourceAdmin(MPTTModelAdmin):
    save_on_top = True
    list_display_links = ("name",)
    list_display = ['name', 'parent','slug', 'published']
    prepopulated_fields = {'slug': ('name',)}
    # list_editable = ['description',]
    mptt_level_indent = 20






class ResourceAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title', 'published_date', 'get_name_gategory', 'published', 'views',]

    list_display_links = ("title",)
    prepopulated_fields = {'slug': ('title',)}


    list_editable = ('published',)
    readonly_fields = ('views', 'edit_date',)
    list_filter = ('category',)

    filter_horizontal = ('category',)


admin.site.register(Resource, ResourceAdmin)
admin.site.register(CategoryResource, CategoryResourceAdmin)