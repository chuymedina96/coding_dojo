# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-20 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register_app', '0004_auto_20191020_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=255, null=True),
        ),
    ]