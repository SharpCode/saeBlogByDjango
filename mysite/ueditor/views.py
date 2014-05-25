from django.http import HttpResponse
from django.utils import simplejson
from datetime import datetime
from mysite.settings import PROJECT_ROOT

import sae.storage
domain_name = "luoming"           
          
    
	
def controller(request):
	action=request.GET['action']
	possibles=globals().copy()
	possibles.update(locals())
	method=possibles.get(action)
	if method:
		return method(request)
	else:
		return HttpResponse('no action match')

def config(request):
	fd=open(PROJECT_ROOT+'/static/js/ueditor/config.json')
	json=fd.read()
	fd.close()
	return HttpResponse(json)

def uploadfile(request):
	name=request.POST['name']
	return upload_file(request,"files/"+name)

def uploadimage(request):	
	name=datetime.now().strftime('%Y%m%d%H%M%S%f.png')
	return upload_file(request,"images/"+name)

def listfile(request):
	return list_file(request,"/images/")

def listimage(request):
	return list_file(request,"/files/")

def handle_file(f,name):
    s = sae.storage.Client()
    ob = sae.storage.Object(f.read())  
    url = s.put(domain_name, name, ob)  
    return url
    
def list_file(request,dir_name):
    start=(int)(request.GET['start'])
    size=(int)(request.GET['size'])
    s=sae.storage.Client()
    files_all=s.list(dir_name)
    files=images_all[start:start+size]
    json={
		'state':'SUCCESS',
		'list':map(lambda x:{'url':x},images),
		'start':start,
		'size':len(files),
		'total':len(files_all)
	}
    response=HttpResponse(simplejson.dumps(json,ensure_ascii=False))
    response['Content-Type']='text/plain'
    return response

def upload_file(request,name):
	url=handle_file(request.FILES['upfile'],name)
	json={
		'url':url,
		'state':'SUCCESS',
	}
	response=HttpResponse(simplejson.dumps(json,ensure_ascii=False))
	response['Content-Type']='text/plain'
	return response
