# Generated by Django 2.2.24 on 2023-02-27 17:23

from django.db import migrations


def fill_new_buildings(apps, schema_editor):

    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.new_building = False
        if flat.construction_year >= 2015:
            flat.new_building = True
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_buildings)
    ]