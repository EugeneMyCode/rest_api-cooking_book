# Generated by Django 4.0.2 on 2022-02-06 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_ingredient_weigth_kg_ingredient_weigthkg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='weigthkg',
        ),
    ]