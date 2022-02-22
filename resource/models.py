from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class CategoryResource(MPTTModel):
    """Класс модели категорий сетей"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительская категория",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    published = models.BooleanField("Отображать?", default=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('blog:post_lists', kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Категория ресурса"
        verbose_name_plural = "Категории ресурсов"


class Resource(models.Model):
    """Класс модели поста"""
    title = models.CharField("Заголовок", max_length=500)
    slug = models.SlugField("url", max_length=50, unique=True)
    text = RichTextUploadingField(verbose_name="Содержание")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    edit_date = models.DateTimeField(
        "Дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        "Дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField("Главная фотография", upload_to="uploads/resource/%Y/%m/%d/", blank=True, null=True)
    category = models.ForeignKey(
        CategoryResource,
        verbose_name="Категория", on_delete=models.CASCADE
    )
    published = models.BooleanField("Опубликовать?", default=True)
    views = models.PositiveIntegerField("Просмотрено", default=0)

    def get_name_gategory(self):
        return '\n, \n '.join([str(child.name) for child in self.category.all()])

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

class FileItem(models.Model):

    file = models.FileField(upload_to='uploads/resource/file/%Y/%m/%d', verbose_name='Документы для прикрепление', blank=True, null=True, unique=True, help_text="загружать только pdf")

    doc = models.ForeignKey(Resource, related_name='fileitems', on_delete=models.CASCADE, help_text="Pdf файлы" )
    description = models.CharField("Краткое описание ", max_length=250, default='', blank=True, null=True)

    def __str__(self):

        return str(self.doc.id)

    class Meta:

        verbose_name = "Файл pdf"

        verbose_name_plural = "Файлы pdf"