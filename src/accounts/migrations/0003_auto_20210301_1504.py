# Generated by Django 3.1.7 on 2021-03-01 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210228_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', through='accounts.FollowRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
