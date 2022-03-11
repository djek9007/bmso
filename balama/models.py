from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Create your models here.
class Baspa(models.Model):
    """База издательств"""
    name = models.CharField(_('Наименование издательства'), max_length=200)

    def __str__(self):
        return self.name

class Language(models.Model):
    """Язык учебника русс каз англ. """
    name = models.CharField(_('Наименование языка обучения'), max_length=200)

    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    """Параллеь 1 2 3 4 итд класс """
    name = models.CharField(_('Наименование класса/параллеля'), max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    """Авторы книг"""
    name = models.CharField(_('Автор'), max_length=200)

    def __str__(self):
        return self.name

class VersionBook(models.Model):
    """Версия учебника бумажный или электронный"""
    name = models.CharField(_('Вид учебника'), max_length=200)

    def __str__(self):
        return self.name

class YearLearning(models.Model):
    """Год издание книги"""
    name = models.CharField('Год издание', max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """" Учебник """
    baspa = models.ForeignKey(Baspa, verbose_name='Издательство', on_delete=models.CASCADE)
    name = models.CharField(_('Наименование предмета'), max_length=200)
    versionBook = models.ForeignKey(VersionBook, verbose_name='Вид учебника', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name='Язык', on_delete=models.CASCADE)
    yearLearning = models.ForeignKey(YearLearning, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, verbose_name='Автор/ы учебника', on_delete=models.CASCADE)
    classRoom = models.ForeignKey(ClassRoom, verbose_name='Класс/параллель', on_delete=models.CASCADE)

    def __str__(self):
        return self.name