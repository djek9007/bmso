# Generated by Django 3.2.9 on 2022-03-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20220309_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='albom',
            name='image',
            field=models.ImageField(blank=True, help_text='Размеры фото 300*206', null=True, upload_to='uploads/photo/albom/%Y/%m/%d/', verbose_name='Обложка'),
        ),
    ]