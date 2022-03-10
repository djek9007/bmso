from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.flatpages.models import FlatPage
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from blog.models import Category,  Post, PhotoItem, FileItem


class PhotoItemInline(admin.TabularInline):
    model = PhotoItem
    extra = 2
class FileItemInline(admin.TabularInline):
    model = FileItem
    extra = 2
class CategoryAdmin(MPTTModelAdmin):
    save_on_top = True
    list_display_links = ("name",)
    list_display = ['name', 'parent','slug', 'published']
    prepopulated_fields = {'slug': ('name',)}
    # list_editable = ['description',]
    mptt_level_indent = 20


# class TagAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'published']
#     prepopulated_fields = {'slug': ('name',)}



class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['title', 'published_date',  'published', 'views',]

    list_display_links = ("title",)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotoItemInline, FileItemInline]

    list_editable = ('published',)
    readonly_fields = ('views', 'edit_date',)
    list_filter = ('category',)


    def thumb_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=50,
            height=50,
        )
        )

    thumb_image.short_description = "Миниатюра"

class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


admin.site.register(Post, PostAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Category, CategoryAdmin)