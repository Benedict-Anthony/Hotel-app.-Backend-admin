# Generated by Django 4.1.5 on 2023-02-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0020_remove_accommodationimages__first_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationimages',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='accommodation_images'),
        ),
    ]