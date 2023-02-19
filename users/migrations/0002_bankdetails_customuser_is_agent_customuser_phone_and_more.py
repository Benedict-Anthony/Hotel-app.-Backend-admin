# Generated by Django 4.1.5 on 2023-02-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255, verbose_name='Bank Name')),
                ('account_number', models.CharField(max_length=255, verbose_name='Account Number')),
                ('account_name', models.CharField(max_length=255, verbose_name='Account Name')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.CreateModel(
            name='HouseAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('NIN', models.CharField(max_length=255, verbose_name='NIN')),
                ('valid_id', models.ImageField(blank=True, null=True, upload_to='house_agent', verbose_name='Valid ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='house_agent', verbose_name='Image')),
                ('bank_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='house_agent', to='users.bankdetails')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='house_agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]