# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apollo_release', '0003_app_branch_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_branch',
            name='latest_commit',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
