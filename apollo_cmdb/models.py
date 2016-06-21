from __future__ import unicode_literals

from django.db import models



# Create your models here.

ACTIVE_STATUS = (
    (0, 'offline'),
    (1, 'online'),
)

ENV_TYPE = (
    (1, 'DEV'),
    (2, 'SIT'),
    (3, 'PRE'),
    (4, 'BETA'),
    (5, 'ONLINE'),
)

class app_env(models.Model):
    app_id=models.IntegerField(default=0)
    #app_id=models.ForeignKey(application)
    name=models.CharField(max_length=20)
    type=models.IntegerField(choices=ENV_TYPE, default=1)
    status=models.IntegerField(choices=ACTIVE_STATUS, default=1)
    create_time=models.DateTimeField(auto_now_add=True)
    owner=models.CharField(max_length=20)
    ip_list=models.CharField(max_length=500,default="null")

class ip_info(models.Model):
    env_id=models.ForeignKey(app_env)
