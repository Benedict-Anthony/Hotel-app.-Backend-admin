# Generated by Django 4.1.5 on 2023-02-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0017_accommodationspace_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationspace',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accommodationspace',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]