# Generated by Django 3.2.9 on 2022-03-09 05:23

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='url')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/blog/%Y/%m/%d/', verbose_name='Главное фото меню')),
                ('stroke', models.BooleanField(default=False, verbose_name='Меню на 1 строке')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menu', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
