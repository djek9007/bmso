from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.urls import reverse


class Year(models.Model):
    year = models.CharField(_('Год'), max_length=100, unique=True)
    image = models.ImageField(upload_to='uploads/photo/albom/%Y/%m/%d/', verbose_name='Обложка', blank=True, null=True,
                               help_text="Размеры фото 300*206")
    slug = models.SlugField("url", max_length=50, unique=True)
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.year
    def get_absolute_url(self):
        return reverse('gallery:gallery_list', kwargs={'albom_slug': self.slug})

    class Meta:

        verbose_name = "Год архива"
        verbose_name_plural = "Года архива"


class Albom(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, verbose_name='Год')
    name = models.CharField(_('Наименование альбома'), max_length=200)
    slug = models.SlugField("url", max_length=50, unique=True)
    image = models.ImageField(upload_to='uploads/photo/albom/%Y/%m/%d/', verbose_name='Обложка', blank=True, null=True,
                              help_text="Размеры фото 300*206")
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery:gallery_detail', kwargs={'year_slug': self.year.slug,'albom_slug': self.slug})

    class Meta:

        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"



class PhotoItem(models.Model):

    image = models.ImageField(upload_to='uploads/photo/albom/%Y/%m/%d/', verbose_name='Галерея', blank=True, null=True, unique=True, help_text="Размеры фото 360*560")

    photo = models.ForeignKey(Albom, related_name='photoitems', on_delete=models.CASCADE, help_text="Размеры фото 455*565" )
    description = models.CharField(_("Краткое описание фото"), max_length=250, default='', blank=True, null=True)

    def __str__(self):

        return str(self.photo.id)

    class Meta:

        verbose_name = "Фотоархив"

        verbose_name_plural = "Фотоархивы"
