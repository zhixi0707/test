# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apollo_release', '0015_auto_20160623_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_int_node',
            name='commit',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
