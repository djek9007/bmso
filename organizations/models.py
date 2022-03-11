import csv

from django.db import models
from django.http import HttpResponse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class Region(models.Model):
    """Модель таблицы области"""
    name = models.CharField(_('Область'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class District(models.Model):
    """Модель таблицы Района"""
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.CASCADE)
    name = models.CharField(_('Район'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"


class Locality(models.Model):
    """Модель таблицы населенного пункта"""
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name='Область', on_delete=models.CASCADE)
    name = models.CharField(_('Населенный пункт'), max_length=100)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенные пункты"

class TerritorialAffiliation(models.Model):
    """Модель таблицы территориальная принадлежность город село"""

    name = models.CharField(_('Область'), max_length=100, unique=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Территориральная принадлежность"
        verbose_name_plural = "Территориальные принадлежности"


class Organization(models.Model):
    """Модель таблицы организации"""
    region = models.ForeignKey(Region, verbose_name='Область', on_delete=models.CASCADE)
    district = models.ForeignKey(District, verbose_name='Область', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name='Населенный пункт', on_delete=models.CASCADE)
    territoriAlaffiliation = models.ForeignKey(TerritorialAffiliation, verbose_name='Территориральная принадлежность', on_delete=models.CASCADE)
    name = models.CharField(_('Наименование организации'), max_length=100,)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True, blank=True, null=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published = models.BooleanField("Опубликовать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"