# -*- coding: UTF-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

#包装csrf请求，避免django认为其实跨站攻击脚本
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import app_env
from apollo_release.models import application


@csrf_exempt
def app_cmdb(request):
    limit = 10  # 每页显示的记录数
    app_id=request.GET.get('app_id')
    data = application.objects.all()
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('app_cmdb.html',{'data':data})

def app_env_mng(request):
    #limit = 10  # 每页显示的记录数
    app_id=request.GET.get('app_id')
    env_list=app_env.objects.filter(app_id=app_id)

    return render(request, 'app_env_mng.html',locals())

# 新增app env信息
def app_env_add(request):
    app_id=request.POST['app_id']
    name=request.POST['name']
    status=request.POST['status']
    type=request.POST['type']
    owner=request.POST['owner']
    ip_list=request.POST['ip_list']
    data=app_env()
    data.name=name
    data.status=status
    data.app_id=app_id
    data.type=type
    data.owner=owner
    data.ip_list=ip_list
    data.save()

    env_list=app_env.objects.filter(app_id=app_id)
    return render(request, 'app_env_mng.html',locals())