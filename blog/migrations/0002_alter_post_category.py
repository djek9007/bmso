# Generated by Django 3.2.9 on 2021-11-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='Категория'),
        ),
    ]
