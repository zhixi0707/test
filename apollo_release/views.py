# -*- coding: UTF-8 -*-
from django.shortcuts import render
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

from .models import product, application, app_branch
from apollo_cmdb.models import app_env

import release_common


@csrf_exempt
def index(request):
    return render(request,'index.html')

def prod_new(request):
    #return render_to_response('prod_new.html',context_instance = RequestContext(request))
    return render(request,'prod_new.html')

def prod_query(request):
    limit = 5  # 每页显示的记录数
    data = product.objects.all()
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('prod_curd.html',{'data':data})

# 新增prod信息
def prod_add(request):
    name=request.POST['name']
    status=request.POST['status']
    owner=request.POST['owner']
    note=request.POST['note']
    data=product()
    data.name=name
    data.status=status
    data.owner=owner
    data.note=note
    data.save()
    return HttpResponseRedirect("prod_query")

# 更新prod信息
def prod_update(request):
    id=request.POST['id']
    name=request.POST['name']
    status=request.POST['status']
    owner=request.POST['owner']
    note=request.POST['note']
    data=product.objects.get(id=id)
    data.name=name
    data.status=status
    data.owner=owner
    data.note=note
    data.save()
    return HttpResponseRedirect("prod_query")

#更新一条数据
def prod_showByID(request):
    id=request.GET['id'];
    data=product.objects.get(id=id) #得到具体数据，与filter输出返回类型不同
    return render_to_response('prod_update.html',{'data':data},context_instance = RequestContext(request))

#显示一条prod数据
def prod_queryByID(request):
    id=request.GET['id'];
    if id == "": #若无输入，则转移到query查询所有
        return HttpResponseRedirect("prod_query")
    data=product.objects.filter(id=id) #通过id 过滤结果，是一字典类型
    return render_to_response('prod_curd.html',{'data':data})

#根据id删除一条 prod数据
def prod_deleteByID(request):
    id=request.GET['id'];
    data=product.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect("prod_query")

def app_new(request):
    prod_id=request.GET['prod_id'];
    return render_to_response('app_new.html',{'prod_id':prod_id},context_instance = RequestContext(request))

# 新增app信息
def app_add(request):
    prod_id=request.POST['prod_id']
    name=request.POST['name']
    status=request.POST['status']
    version=request.POST['version']
    version_prefix=request.POST['version_prefix']
    scm_tool=request.POST['scm_tool']
    repo_url=request.POST['repo_url']
    deploy_path=request.POST['deploy_path']
    package_job=request.POST['package_job']
    auto_test_job=request.POST['auto_test_job']
    data=application()
    data.name=name
    data.status=status
    data.prod_id=prod_id
    data.version=version
    data.version_prefix=version_prefix
    data.scm_tool=scm_tool
    data.repo_url=repo_url
    data.repo_name=release_common.gitlabGetRepoName(repo_url)
    data.deploy_path=deploy_path
    data.package_job=package_job
    data.auto_test_job=auto_test_job
    data.save()
    return HttpResponseRedirect("app_query")

def app_query(request):
    limit = 5  # 每页显示的记录数
    data = application.objects.all()
    paginator = Paginator(data, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        data = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        data = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        data = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('app_curd.html',{'data':data})

#显示一条app数据
def app_queryByID(request):
    id=request.GET['id'];
    if id == "": #若无输入，则转移到query查询所有
        return HttpResponseRedirect("app_query")
    data=application.objects.filter(id=id) #通过id 过滤结果，是一字典类型
    return render_to_response('app_curd.html',{'data':data})

#根据id删除一条 prod数据
def app_deleteByID(request):
    id=request.GET['id']
    data=application.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect("app_query")

def app_showByID(request):
    id=request.GET['id']
    data=application.objects.get(id=id) #得到具体数据，与filter输出返回类型不同
    return render_to_response('app_update.html',{'data':data},context_instance = RequestContext(request))

# 更新app信息
def app_update(request):
    id=request.POST['id']
    prod_id=request.POST['prod_id']
    name=request.POST['name']
    status=request.POST['status']
    version=request.POST['version']
    version_prefix=request.POST['version_prefix']
    repo_url=request.POST['repo_url']
    deploy_path=request.POST['deploy_path']
    package_job=request.POST['package_job']
    auto_test_job=request.POST['auto_test_job']

    data=application.objects.get(id=id)
    data.name=name
    data.status=status
    data.version=version
    data.version_prefix=version_prefix
    data.repo_url=repo_url
    data.repo_name=release_common.gitlabGetRepoName(repo_url)
    data.deploy_path=deploy_path
    data.package_job=package_job
    data.auto_test_job=auto_test_job
    data.save()
    return HttpResponseRedirect("app_query")

def app_ws(request):
    id=request.GET['id']
    app=application.objects.get(id=id)
    prod_id=app.prod_id
    prod=product.objects.get(id=prod_id)
    #return render_to_response('app_update.html',{'data':app},context_instance = RequestContext(request))
    #return render_to_response('app_test.html',{'prod_data':prod})
    return render(request, 'app_ws.html',locals())

def app_br_mng(request):
    app_id=request.GET['app_id']
    app=application.objects.get(id=app_id)

    branches=app_branch.objects.filter(app_id=app_id).order_by("-create_time")
    #return render_to_response('app_update.html',{'data':app},context_instance = RequestContext(request))
    #return render_to_response('app_test.html',{'prod_data':prod})
    return render(request, 'app_br_mng.html',locals())

# 新增prod信息
def app_br_add(request):
    app_id=request.POST['app_id']
    name=request.POST['name']
    status=request.POST['status']
    type=request.POST['type']
    purpose=request.POST['purpose']
    dev_list=request.POST['dev_list']
    qa_list=request.POST['qa_list']

    data=app_branch()
    data.app_id=app_id
    data.name=name
    data.status=status
    data.type=type
    data.purpose=purpose
    data.dev_list=dev_list
    data.qa_list=qa_list

    app=application.objects.get(id=app_id)
    result=release_common.gitlabCreateBranch(app.repo_name,name)
    if result == release_common.SUCCESS :
        data.save()
        branches=app_branch.objects.filter(app_id=app_id).order_by("-create_time")
        #return HttpResponseRedirect("app_br_mng",{'app_id':app_id})
        ###!!!! here the paginator has problem, cannot view "next page" !!####
        limit = 10  # 每页显示的记录数
        paginator = Paginator(branches, limit)  # 实例化一个分页对象
        page = request.GET.get('page')  # 获取页码
        try:
            branches = paginator.page(page)  # 获取某页对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            branches = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大，没有相应的记录
            branches = paginator.page(paginator.num_pages)  # 取最后一页的记录
        return render(request, 'app_br_mng.html',locals())
    else:
        return HttpResponseRedirect("app_query")

    # 新增dev process management
    # to bo finished
def app_dev_mng(request):
    app_id=request.GET['app_id']
    app=application.objects.get(id=app_id)
    dev_branch=app_branch.objects.filter(app_id=app_id)
    dev_env=app_env.objects.filter(app_id=app_id)

    #get the open dev node for this app, maybe including the branch info

    return render(request, 'app_dev_mng.html',locals())

def new_app_dev_node(request):
    app_id=request.POST['app_id']
    branch=request.POST['branch']
    env=request.POST['env']
    commit=request.POST['commit']
    #print (app_id)
    #print (branch)
    #print (env)
    #print (commit)
    #dev_branch=app_branch.objects.filter(app_id=app_id)
    #dev_env=app_env.objects.filter(app_id=app_id)
    #return render_to_response('app_dev_node.html',{'data':data},context_instance = RequestContext(request))
    return HttpResponseRedirect("app_query")

