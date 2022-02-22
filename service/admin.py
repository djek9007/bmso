from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from service.models import CategoryService, Service, FileItem


class CategoryServiceAdmin(MPTTModelAdmin):
    save_on_top = True
    list_display_links = ("name",)
    list_display = ['name', 'parent', 'slug', 'published']
    prepopulated_fields = {'slug': ('name',)}
        # list_editable = ['description',]
    mptt_level_indent = 20

class FileItemInline(admin.TabularInline):
    model = FileItem
    extra = 2


class ServiceAdmin(admin.ModelAdmin):

    list_display = ['title', 'published_date', 'categoryservice', 'published', 'views',]

    list_display_links = ("title",)
    prepopulated_fields = {'slug': ('title',)}

    inlines = [FileItemInline]
    list_editable = ('published',)
    readonly_fields = ('views', 'edit_date', 'thumb_image',)
    list_filter = ('categoryservice',)
    save_on_top = True

    def thumb_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=50,
            height=50,
        )
        )

    thumb_image.short_description = "Миниатюра"


admin.site.register(Service, ServiceAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)