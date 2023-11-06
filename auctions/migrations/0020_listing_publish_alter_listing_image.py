# Generated by Django 4.2.3 on 2023-11-06 07:52

import auctions.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=auctions.models.user_directory_path),
        ),
    ]