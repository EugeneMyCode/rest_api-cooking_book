# Generated by Django 4.0.2 on 2022-02-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='weigth_kg',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='weigthkg',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
