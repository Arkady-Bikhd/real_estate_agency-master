# Generated by Django 2.2.24 on 2023-02-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20230227_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(blank=True, verbose_name='Новостройка'),
        ),
    ]
