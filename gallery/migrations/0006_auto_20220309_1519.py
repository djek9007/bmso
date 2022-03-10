# Generated by Django 3.2.9 on 2022-03-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20220309_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='image',
            field=models.ImageField(blank=True, help_text='Размеры фото 300*206', null=True, upload_to='uploads/photo/albom/%Y/%m/%d/', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=100, unique=True, verbose_name='Год'),
        ),
    ]
