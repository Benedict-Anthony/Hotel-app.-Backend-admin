# Generated by Django 4.1.5 on 2023-02-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0009_accommodationimages_first_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodationimages',
            old_name='first_thumbnail',
            new_name='_first_thumbnail',
        ),
        migrations.AddField(
            model_name='accommodationimages',
            name='_second_thumbnail',
            field=models.ImageField(blank=True, upload_to='accommodation_images'),
        ),
        migrations.AddField(
            model_name='accommodationimages',
            name='_third_thumbnail',
            field=models.ImageField(blank=True, upload_to='accommodation_images'),
        ),
    ]
