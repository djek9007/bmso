from django.apps import AppConfig


class ResourceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resource'
    verbose_name = 'Ресурс'
    verbose_name_plural = 'Ресурсы'