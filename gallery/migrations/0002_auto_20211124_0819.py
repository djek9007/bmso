# Generated by Django 3.2.9 on 2021-11-24 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CategoryPhoto',
            new_name='Albom',
        ),
        migrations.AlterModelOptions(
            name='albom',
            options={'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
    ]