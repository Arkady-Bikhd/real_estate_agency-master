# Generated by Django 2.2.24 on 2023-02-28 18:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
