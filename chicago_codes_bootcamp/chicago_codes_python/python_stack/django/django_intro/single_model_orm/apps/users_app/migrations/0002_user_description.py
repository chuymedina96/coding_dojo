# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-09 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default='something that is default', max_length=255),
            preserve_default=False,
        ),
    ]