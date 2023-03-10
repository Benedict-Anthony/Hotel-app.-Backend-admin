# Generated by Django 4.1.5 on 2023-03-09 13:09

import accommodation.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.CharField(default=accommodation.models.customId, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('distance', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('banner', models.ImageField(blank=True, null=True, upload_to='accommodation_images')),
                ('available', models.BooleanField(default=True)),
                ('pinned', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Accommodation Spaces',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Accommodation Categories',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.CharField(default=accommodation.models.customId, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='accommodation_images')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='accommodation_images')),
            ],
            options={
                'verbose_name_plural': 'Accommodation Images',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
