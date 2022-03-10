from django.db import models

# Create your models here.
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(MPTTModel):
    """Класс модели меню"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=50, unique=True, blank=True, null=True )
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    published = models.BooleanField("Отображать?", default=True)
    image = models.ImageField("Главное фото меню", upload_to="uploads/blog/%Y/%m/%d/", blank=True, null=True)
    stroke = models.BooleanField(default=False, verbose_name='Меню на 1 строке')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:service_lists', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    class MPTTMeta:
        order_insertion_by = ['parent',]