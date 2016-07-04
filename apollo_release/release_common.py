import requests
from .models import product, application, app_branch, app_dev_node, app_int_node, app_process_dev
from apollo_cmdb.models import app_env

GITLAB_URL = "http://gitlab.mogujie.org/"
GITLAB_KEY = '3TfHCNJWQ9nb-HNxhNhX'
GITLAB_REF = 'master'
GITLAB_API = 'http://gitlab.mogujie.org/api/v3/projects/'

SUCCESS = 1
FAIL = 0

JENKINS_TOKEN='ci_scm'

def node_prehook_act(env,stage,node_id,status):
    #env=request.GET['env']
    #stage=request.GET['stage']
    #node_id=request.GET['node_id']
    #status=request.GET['status']
    print "env is " + env
    print "stage is " + stage
    print "node_id is " + node_id
    print "status is " + status
    if env == "dev":
        dev_node=app_dev_node.objects.get(id=node_id)
        if stage == "package":
            dev_node.package_status=status
        elif stage == "deploy":
            dev_node.deploy_status=status
        elif stage == "test":
            dev_node.test_status=status
        else:
            print "no stage matched!"

        dev_node.save()
        return "success"
    else:
        print "no env matched!!"
        print "error"

def node_posthook_act(env,stage,node_id,status):
    print "env is " + env
    print "stage is " + stage
    print "node_id is " + node_id
    print "status is " + status
    next_stage=""
    if env == "dev":
        dev_node=app_dev_node.objects.get(id=node_id)
        if stage == "package":
            dev_node.package_status=status
            next_stage="deploy"
        elif stage == "deploy":
            dev_node.deploy_status=status
            next_stage="test"
        elif stage == "test":
            dev_node.test_status=status
            next_stage="end"
        else:
            print "no stage matched!"

        dev_node.save()
        if stage == "end":
            print "process stage is finished"
        else:
            if status == "success":
                startDevNode(dev_node.app_id,node_id,next_stage)
        return "success"
    else:
        print "no env matched!!"
        print "error"

def startDevNode(app_id,node_id,stage):
    app_info=application.objects.get(id=app_id)
    node_info=app_dev_node.objects.get(id=node_id)
    process_info=app_process_dev.objects.get(app_id=app_id)
    if stage == "package":
        if process_info.auto_package == "true":
            args="&node_id=" + str(node_id) + "&env=dev"
            startJenkins(app_info.package_job,args)
    elif stage == "deploy":
        if process_info.auto_deploy == "true":
            args="&node_id=" + str(node_id) + "&env=dev"
            startJenkins(app_info.deploy_job,args)
    elif stage == "test":
        if process_info.auto_test == "true":
            args="&node_id=" + str(node_id) + "&env=dev"
            startJenkins(app_info.auto_test_job,args)
    else:
        print "no stage definied"

def gitlabGetRepoName(repo):
    global GITLAB_URL
    global GITLAB_KEY
    print ("repo is:" + repo)
    repo_name=repo.replace(GITLAB_URL,'')
    repo_name=repo_name.replace('/','%2F')
    repo_name=repo_name.replace('.git','')
    return repo_name
    #url=GITLAB_URL + '/api/v3/projects/' + repo_name + '?private_token=' + GITLAB_KEY
    #print url
    #r=requests.get(url)
    #print r.text

def gitlabCreateBranch(repo_name,branch_name):
    url= GITLAB_API + repo_name + '/repository/branches'
    data={'private_token':GITLAB_KEY,'branch_name':branch_name,'ref':GITLAB_REF}
    r=requests.post(url,data)
    print url
    print repo_name
    print branch_name
    print GITLAB_KEY
    print r.status_code
    print r.text
    if r.status_code == 200 or r.status_code == 201  :
        print ('success!!')
        return SUCCESS
    else:
        print ('branch creation fail')
        return FAIL

def startJenkins(job,args):
    url=job + '/buildWithParameters?' + 'token=' + JENKINS_TOKEN + args
    print url
    r=requests.get(url)
    print r.status_code
    if r.status_code == 200 or r.status_code == 201  :
        print ('success!!')
        return SUCCESS
    else:
        print ('branch creation fail')
        return FAIL

def compare(x):
    if x == 200 or x == 201 :
        print "success"
    else:
        print "fail"