# Generated by Django 3.2.9 on 2021-12-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0005_slide_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Главное фото?'),
        ),
    ]