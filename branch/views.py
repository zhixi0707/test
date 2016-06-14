# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.
# for bootstrap test

#包装csrf请求，避免django认为其实跨站攻击脚本
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.shortcuts import render_to_response

from .models import Applications, Branch

def home(request):
        return render(request,'add_app_base.html')

def index(request):
        return render(request,'home.html')

@csrf_exempt

# 添加app信息
def addApplication(request):
    name=request.POST['name']
    status=request.POST['status']
    app=Applications()
    app.name=name
    app.status=status
    app.save()
    return HttpResponseRedirect("/app_q")

#查询所有，并分页显示
def app_query(request):
    limit = 5  # 每页显示的记录数
    #students = Student.objects.all()
    apps = Applications.objects.all()
    paginator = Paginator(apps, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        apps = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        apps = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        apps = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('app_curd_new.html',{'data':apps})

#删除数据
def app_delByID(request):
    id=request.GET['id'];
    app=Applications.objects.get(id=id)
    app.delete()
    return HttpResponseRedirect("/app_q")

#更新一条数据
def app_showUid(request):
    id=request.GET['id'];
    app=Applications.objects.get(id=id) #得到具体数据，与filter输出返回类型不同
    return render_to_response('app_update.html',{'data':app})

#显示一条数据
def app_queryById(request):
    id=request.GET['id'];
    if id == "": #若无输入，则转移到query查询所有
        return HttpResponseRedirect("/app_q")
    app=Applications.objects.filter(id=id) #通过id 过滤结果，是一字典类型
    return render_to_response('app_curd.html',{'data':app})