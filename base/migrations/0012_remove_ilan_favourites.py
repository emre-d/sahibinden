# Generated by Django 4.1 on 2022-12-22 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_ilan_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ilan',
            name='favourites',
        ),
    ]
