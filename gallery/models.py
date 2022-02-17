from django.db import models

# Create your models here.
class Year(models.Model):
    year = models.CharField('Год', max_length=100)

    def __str__(self):
        return self.year

    class Meta:

        verbose_name = "Год архива"
        verbose_name_plural = "Года архива"

class Albom(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, verbose_name='Год')
    name = models.CharField('Наименование альбома', max_length=200)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

class PhotoItem(models.Model):

    image = models.ImageField(upload_to='uploads/photo/albom/%Y/%m/%d/', verbose_name='Галерея', blank=True, null=True, unique=True, help_text="Размеры фото 360*560")

    photo = models.ForeignKey(Albom, related_name='photoitems', on_delete=models.CASCADE, help_text="Размеры фото 455*565" )
    description = models.CharField("Краткое описание фото", max_length=250, default='', blank=True, null=True)

    def __str__(self):

        return str(self.photo.id)

    class Meta:

        verbose_name = "Фотоархив"

        verbose_name_plural = "Фотоархивы"
