from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import project,module
import requests
import json
# Create your views here.

@login_required
def manage(request):
	return render(request,'cases.html',{'type':'list'})

@login_required
def debug(request):
	if request.method == 'GET':
		projects = project.objects.all()
		return render(request,'debug.html',{'type':'debug','projects':projects})
	elif request.method == 'POST':
		print("6666")
		pid = request.POST.get('get_project')
		print(pid)
		if pid :
			pro = project.objects.get(id=pid)
			modules = module.objects.filter(project=pro)
			print(pro,modules)
			return HttpResponse(modules)

@login_required
def api_debug(request):
	if request.method == 'POST':
		url = request.POST.get("url",'')
		method = request.POST.get('method','get')
		params = request.POST.get('params','{}')
		header = request.POST.get('header','{}')
		datatpye = request.POST.get("datatype")

		if url.startswith('https://') or url.startswith('http://'):
			pass 
		else:
			return HttpResponse(f'url:{url} 的格式不正确')


		try:
			data = json.loads(params.replace("'", "\""))
		except :
			return HttpResponse(f'参数：{params} 不是dict 格式')

		
		try:
			head_json = json.loads(header.replace("'","\""))
		except :
			return HttpResponse(f'header：{header} 不是dict 格式')

		if method == 'get':
			if params == '' and header == '' :
				r = requests.get(url)
			elif params == '' and header != '' :
				r = requests.get(url, headers=head_json)
			elif params != '' and header == '':
				r = requests.get(url, params = data)
			else:
				r = requests.get(url, params = data, headers=head_json)

		if method == 'post':
			if params == '':
				if header == '' :
					r = requests.post(url)
				else:
					r = requests.post(url, headers=head_json)
			else:
				if datatpye == 'form':
					if header == '':
						r = requests.post(url, data = data)
					else:
						r = requests.post(url, data = data, headers=head_json)
				if datatpye == 'json':
					if header == '':
						r = requests.post(url, json = data)
					else:
						r = requests.post(url, json = data, headers=head_json)

		# 必须返回HttpResoponse
		return HttpResponse(r.content.decode('utf-8'))
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def save(request):
	if request.method == 'POST':
		url = request.POST.get("url",'')
		method = request.POST.get('method','get')
		params = request.POST.get('params','{}')
		header = request.POST.get('header','{}')
		datatpye = request.POST.get("datatype")
	else:
		return HttpResponse("404")