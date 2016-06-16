"""scm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from branch import views as branch_views # from branch app
from apollo_release import views as release_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # for test purpose
    #url(r'^home/', branch_views.home, name='home'),
    #url(r'^addApplication$', branch_views.addApplication, name='addApplication'),
    #url(r'^app_q$',branch_views.app_query,name='app_query'),
    #url(r'^app_delete$',branch_views.app_delByID,name='app_delByID'),
    #url(r'^app_showid$',branch_views.app_showUid,name='app_showUid'),
    #url(r'^app_query$',branch_views.app_queryById,name='app_queryById'),
    #url(r'^index$',branch_views.index,name='index'),

    # for index page
    url(r'^index$', release_views.index, name='index'),

    # for release application
    # for product management
    url(r'^prod_query$',release_views.prod_query,name='prod_query'),
    url(r'^prod_queryByID$',release_views.prod_queryByID,name='prod_queryByID'),
    url(r'^prod_new$',release_views.prod_new,name='prod_new'),
    url(r'^prod_add$',release_views.prod_add,name='prod_add'),
    url(r'^prod_update$',release_views.prod_update,name='prod_update'),
    url(r'^prod_deleteByID$',release_views.prod_deleteByID,name='prod_deleteByID'),
    url(r'^prod_showByID$',release_views.prod_showByID,name='prod_showByID'),

    # for application management
    url(r'^app_new$',release_views.app_new,name='app_new'),
    url(r'^app_add$',release_views.app_add,name='app_add'),
    url(r'^app_query$',release_views.app_query,name='app_query'),
    url(r'^app_queryByID$',release_views.app_queryByID,name='app_queryByID'),
    url(r'^app_deleteByID$',release_views.app_deleteByID,name='app_deleteByID'),
    url(r'^app_showByID$',release_views.app_showByID,name='app_showByID'),
    url(r'^app_update$',release_views.app_update,name='app_update'),

    # for application workspace management
    url(r'^app_dev_ws$',release_views.app_dev_ws,name='app_dev_ws'),
    url(r'^app_br_mng$',release_views.app_br_mng,name='app_br_mng'),
    url(r'^app_br_add$',release_views.app_br_add,name='app_br_add'),

    # for cmdb application


    # for rca application

    # for user management
    
]
