# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apollo_release', '0004_app_branch_latest_commit'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='repo_name',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
