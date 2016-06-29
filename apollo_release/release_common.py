import requests

GITLAB_URL = "http://gitlab.mogujie.org/"
GITLAB_KEY = '3TfHCNJWQ9nb-HNxhNhX'
GITLAB_REF = 'master'
GITLAB_API = 'http://gitlab.mogujie.org/api/v3/projects/'

SUCCESS = 1
FAIL = 0

JENKINS_TOKEN='ci_scm'

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