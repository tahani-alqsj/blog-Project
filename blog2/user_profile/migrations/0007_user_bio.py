# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_user_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(default='this user has no bio', max_length=1000),
        ),
    ]
