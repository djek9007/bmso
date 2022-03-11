from import_export import resources, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import District, Region



#https://django-import-export.readthedocs.io/en/stable/installation.html#example-app
class RegionResource(resources.ModelResource):
    """Django export class for model Region"""

    class Meta:
        model = Region
        exclude = ('id', 'created_date', 'edit_date', 'published',)
        # export_order = ('name',)
        fields = ('name',)
        import_id_fields = ('name',)


class DistrictResource(resources.ModelResource):
    """Django export class for model District"""
    # name = Field(attribute='name', column_name = District.name.field.verbose_name)
    # region = fields.Field(attribute='region', column_name='Наименование области', widget=ForeignKeyWidget(Region, 'name'))

    class Meta:
        model = District
        exclude = ('id', 'created_date', 'edit_date', 'published',)
        fields = ('name', 'region',)
        import_id_fields =('name',)

        # skip_unchanged = True
        # report_skipped = True