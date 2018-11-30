import requests
import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from api_app.models import TestCase
from project_app.models import project,module

'''
有关用例的接口
'''

#获取项目-模块信息
def get_project_list(request):
	if request.method == 'GET':
		projects = project.objects.all()
		datalist = []
		for p in projects:
			project_dict = {'name': p.name }
			modules = module.objects.filter(project_id=p.id)
			module_name = []
			if len(modules) != 0:
				for m in modules:
					module_name.append(m.name)
			project_dict['moduleList'] = module_name
			datalist.append(project_dict)
		return JsonResponse({'success':'true','data':datalist})

	else:
		return HttpResponse('404 NOT FOUND')

# 获取用例列表
def cases_list(request):
	if request.method == 'GET':
		projects = project.objects.all()
		cases_list = []

		for p in projects:
			modules = module.objects.filter(project_id=p.id)
			for m in modules:
				cases = TestCase.objects.filter(module_id=m.id)
				if len(cases) !=0:
					for case in cases:
						case_info = p.name + '-->' + m.name + "-->" + case.name
						cases_list.append(case_info)
				else:
					pass
		data = {'caseslist':cases_list}
		return JsonResponse(data)

	else:
		return HttpResponse('404 NOT FOUND')

# 获取用例信息
def cases_info(request):
	if request.method == 'POST':
		cid = request.POST.get('cid','')
		case = TestCase.objects.get(id=cid)
		module_obj = module.objects.get(id=case.module_id)
		project_obj = project.objects.get(id=module_obj.project_id)
		case_info = {
		'name' :case.name,
		'url':case.url,
		'method' :case.method,
		'datatpye' :case.datatpye,
		'headers' : case.headers,
		'params' : case.params,
		'result' : case.result,
		'module_name' : case.module_name,
		'project_name' : project_obj.name
		}
		data = {'success':'true','caseinfo':case_info}
		return JsonResponse(data)
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def api_debug(request):
	'''调试用例'''
	if request.method == 'POST':
		url = request.POST.get("url",'')
		method = request.POST.get('method','')
		params = request.POST.get('params','')
		header = request.POST.get('header','')
		datatpye = request.POST.get("datatype",'')

		if url.startswith('https://') or url.startswith('http://'):
			pass 
		else:
			return HttpResponse(f'url:{url} 的格式不正确')

		if params != '':
			try:
				data = json.loads(params.replace("'", "\""))
			except :
				return HttpResponse(f'参数：{params} 不是dict 格式')

		if header != '':
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
	'''保存测试用例''' 
	if request.method == 'POST':
		name = request.POST.get('name','')
		url = request.POST.get("url",'')
		method = request.POST.get('method','get')
		params = request.POST.get('params','form')
		header = request.POST.get('header','')
		datatpye = request.POST.get("datatype",'')
		module_name = request.POST.get('module_name','')
		project_name = request.POST.get('project_name','')

		if name == '' or url == '':
			return HttpResponse('用例名称或请求url不能为空')
		else:
			module_obj = module.objects.get(name=module_name)
			TestCase.objects.create(project_name=project_name,module=module_obj,name=name, url=url, method=method, params=params,headers=header, datatpye=datatpye)
			return HttpResponse('保存成功')

	else:
		return HttpResponse('请求方法错误')

@login_required
def delete(request,cid):
	'''删除测试用例''' 
	TestCase.objects.get(id=cid).delete()
	return HttpResponseRedirect('/cases/')


@login_required
def update(request):
	'''编辑测试用例''' 
	if request.method == 'POST':
		pass

	else:
		return HttpResponse('请求方法错误')

