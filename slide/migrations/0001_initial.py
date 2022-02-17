# Generated by Django 3.2.9 on 2021-11-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='1920*714', upload_to='', verbose_name='Главное фото для слайдера')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок фото')),
                ('link', models.CharField(max_length=100, verbose_name='Ссылка на статью')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
    ]
