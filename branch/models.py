from __future__ import unicode_literals

from django.db import models

# Create your models here.
#branch status
BRANCH_STATUS = (
               (0, 'new'),
               (1, 'developing'),
               (2, 'integrated'),
               (3, 'released'),
               )

# applications table
class Applications(models.Model):
    name=models.CharField(max_length=20)
    status=models.BooleanField()
    def __unicode__(self):
        return self.name
# branch table
class Branch(models.Model):
    app=models.ForeignKey(Applications)
    name=models.CharField(max_length=20)
    status=models.IntegerField(choices=BRANCH_STATUS, default=0)
    def __unicode__(self):
        return self.name

