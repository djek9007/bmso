from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    """Класс модели категорий сетей"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)
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
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField('Название тега', max_length=100, unique=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    published = models.BooleanField("отображать?", default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={"tag_slug": self.slug})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

# class PostManager(models.Manager):
#     use_for_related_fields = True
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query:
#             or_lookup = (Q(title__icontains=query) | Q(text__icontains=query))
#             qs = qs.filter(or_lookup)
#         return qs


class Post(models.Model):
    """Класс модели поста"""
    title = models.CharField("Заголовок", max_length=500)
    slug = models.SlugField("url", max_length=100, unique=True)
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
    image = models.ImageField("Главная фотография", upload_to="uploads/blog/%Y/%m/%d/")
    category = models.ManyToManyField(
        Category,
        verbose_name="Категория",
    )
    published = models.BooleanField("Опубликовать?", default=True)
    views = models.PositiveIntegerField("Просмотрено", default=0)
    tag = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    # objects = PostManager()

    def get_name_gategory(self):
        return '\n, \n '.join([str(child.name) for child in self.category.all()])

    get_name_gategory.short_description = 'Категории'

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={"category_slug": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']


class PhotoItem(models.Model):

    image = models.ImageField(upload_to='uploads/blog/%Y/%m/%d/', verbose_name='Галерея', blank=True, null=True, unique=True, help_text="Размеры фото 360*560")

    photo = models.ForeignKey(Post, related_name='photoitems', on_delete=models.CASCADE, help_text="Размеры фото 455*565" )
    description = models.CharField("Краткое описание фото", max_length=250, default='', blank=True, null=True)

    def __str__(self):

        return str(self.photo.id)

    class Meta:

        verbose_name = "Галерея постов"

        verbose_name_plural = "Галерея постов"


class FileItem(models.Model):

    file = models.FileField(upload_to='uploads/blog/file/%Y/%m/%d', verbose_name='Документы для прикрепление', blank=True, null=True, unique=True, help_text="загружать только pdf")

    doc = models.ForeignKey(Post, related_name='fileitems', on_delete=models.CASCADE, help_text="Pdf файлы" )
    description = models.CharField("Краткое описание ", max_length=250, default='', blank=True, null=True)

    def __str__(self):

        return str(self.doc.id)

    class Meta:

        verbose_name = "Файл pdf"

        verbose_name_plural = "Файлы pdf"

