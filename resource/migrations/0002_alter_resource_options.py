# Generated by Django 3.2.9 on 2021-11-24 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name': 'Ресурс', 'verbose_name_plural': 'Ресурсы'},
        ),
    ]