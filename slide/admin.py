from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from slide.models import Slide


class SlideAdmin(admin.ModelAdmin):
    list_display = ['thumb_image', 'title', 'link', 'published', 'is_active' ]

    def thumb_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=150,
            height=60,
        )
        )

    thumb_image.short_description = "Миниатюра"

admin.site.register(Slide, SlideAdmin)