# Generated by Django 4.1.5 on 2023-02-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0015_alter_accommodationspace_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationspace',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]