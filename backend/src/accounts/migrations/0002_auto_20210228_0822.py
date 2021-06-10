# Generated by Django 3.1.7 on 2021-02-28 08:22

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='profile_image',
            field=models.ImageField(blank=True, default='no_avatar.png', upload_to=accounts.models.get_image_upload_path),
        ),
    ]