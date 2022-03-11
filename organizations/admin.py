import csv

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from django.http import HttpResponse

from organizations.models import Region, District, Locality, TerritorialAffiliation, Organization
from organizations.resources import DistrictResource, RegionResource


class ActionPublish(admin.ModelAdmin):
    """Action для публикации и снятия с публикации"""

    @admin.action(description='Cнять с публикации')
    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    @admin.action()
    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "% s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)



class DistrictAdmin(ImportExportModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'region',  'published', ]
    actions = ['unpublish', 'publish', ]
    list_display_links = ("name",)
    list_editable = ('published',)
    # readonly_fields = ('published',)
    resource_class = DistrictResource
    actions = ['unpublish', 'publish', ]
    list_filter = ('region',)

    list_per_page = 20

class RegionAdmin(ImportExportModelAdmin, ActionPublish):
    save_on_top = True
    list_display = ['id', 'name', 'published', ]
    actions = ['unpublish', 'publish', ]
    list_display_links = ("name",)
    list_editable = ('published',)
    # readonly_fields = ('published',)
    resource_class = RegionResource
    list_per_page = 20

admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Locality)
admin.site.register(TerritorialAffiliation)
admin.site.register(Organization)