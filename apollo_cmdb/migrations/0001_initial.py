# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app_env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('type', models.IntegerField(choices=[(1, 'DEV'), (2, 'SIT'), (3, 'PRE'), (4, 'BETA'), (5, 'ONLINE')], default=1)),
                ('status', models.IntegerField(choices=[(0, 'offline'), (1, 'online')], default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('owner', models.CharField(max_length=20)),
                ('ip_lists', models.CharField(default='null', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ip_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apollo_cmdb.app_env')),
            ],
        ),
    ]
