# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apollo_release', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_branch',
            name='type',
            field=models.IntegerField(choices=[(0, 'release'), (1, 'develop'), (2, 'other')], default=0),
        ),
    ]
