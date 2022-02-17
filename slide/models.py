from django.db import models

# Create your models here.
class Slide(models.Model):
    image = models.ImageField(verbose_name='Главное фото для слайдера', help_text='1920*714', upload_to='uploads/slide/%Y/%m/%d/')
    title = models.CharField(verbose_name='Заголовок фото', max_length=150, blank=True, null=True)
    link = models.CharField('Ссылка на статью', max_length=100, blank=True, null=True)
    published = models.BooleanField("Опубликовать?", default=True)
    is_active = models.BooleanField("Главное фото?", default=False)


    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"