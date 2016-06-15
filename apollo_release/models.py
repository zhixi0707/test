from __future__ import unicode_literals

from django.db import models

# Create your models here.
BRANCH_STATUS = (
    (0, 'open'),
    (1, 'assigned'),
    (2, 'integrated'),
    (3, 'released'),
    (4, 'ignored'),
)

BRANCH_TYPE = (
    (0, 'release'),
    (1, 'develop'),
    (2, 'other'),
)

ACTIVE_STATUS = (
    (0, 'offline'),
    (1, 'online'),
)

APP_VERSION_STATUS = (
    (0, 'packaged'),
    (1, 'package_fail'),
    (2, 'deployed'),
    (3, 'deploy_fail'),
    (4, 'tested'),
    (5, 'test_fail'),
    (6, 'released'),
    (7, 'release_fail'),
    (8, 'verified'),
    (9, 'verify_fail'),
)

class product(models.Model):
    name=models.CharField(max_length=20)
    status=models.IntegerField(choices=ACTIVE_STATUS, default=1)
    create_time=models.DateTimeField(auto_now_add=True)
    owner=models.CharField(max_length=20)
    #version=models.CharField(max_length=20)
    note=models.TextField()

#class prod_version(models.Model):
#    prod=models.ForeignKey(product)
#    version=models.CharField(max_length=20)
#    create_time=models.DateTimeField(auto_now_add=False)
#    owner=models.CharField(max_length=20)
#    note=models.TextField()

class application(models.Model):
    prod=models.ForeignKey(product)
    name=models.CharField(max_length=20)
    status=models.IntegerField(choices=ACTIVE_STATUS, default=1)
    create_time=models.DateTimeField(auto_now_add=True)
    version=models.CharField(max_length=20,default="null")
    version_prefix=models.CharField(max_length=20,default="null")
    scm_tool=models.CharField(max_length=20,default="null") # git or svn
    repo_url=models.URLField(max_length=300,default="null")
    deploy_path=models.CharField(max_length=50,default="null")
    package_job=models.URLField(max_length=300,default="null")
    auto_test_job=models.URLField(max_length=300,default="null")

class app_version(models.Model):
    prod=models.ForeignKey(application)
    version=models.CharField(max_length=20) # version + env to identify the version
    status=models.IntegerField(choices=APP_VERSION_STATUS, default=0)
    note=models.TextField()
    comments=models.TextField() # record the version action history "who when do what"

class app_branch(models.Model):
    app=models.ForeignKey(application,default=1)
    name=models.CharField(max_length=50,default="null")
    status=models.IntegerField(choices=BRANCH_STATUS, default=1)
    purpose=models.TextField()
    dev_list=models.CharField(max_length=50,default="null")
    qa_list=models.CharField(max_length=50,default="null")
    ## can expend more properties, like "changed files" "lines" "merge_request" "ut_rate" etc

class app_integration(models.Model):
    version=models.CharField(max_length=50,default="null")
    app=models.ForeignKey(application,default=1)
    release_branch=models.OneToOneField(app_branch,default=1)
    dev_branch_list=models.CharField(max_length=100,default="null")# branch id list, use "," to split
    status=models.CharField(max_length=500,default="null") # format "env:status,env:status" to record the progress
    comments=models.TextField(default="null") # record the version action history "who when do what"
    ## can expend more properties, like "fun_test_pass_rate" ......

###################################################################
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
    status=models.IntegerField(choices=BRANCH_STATUS, default=1)
    def __unicode__(self):
        return self.name
