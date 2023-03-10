# Generated by Django 4.1 on 2022-12-04 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_ilan_image1_ilan_image2_ilan_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('tarih', models.DateTimeField(auto_now=True)),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ilan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-tarih'],
            },
        ),
    ]
