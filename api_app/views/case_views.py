import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from api_app.models import TestCase
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''
有关用例的界面显示、操作等
'''

@login_required
def manage(request):
	'''用例管理列表'''
	cases = TestCase.objects.all()
	paginator = Paginator(cases,2)

	page = request.GET.get('page',"1")
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	if request.method == 'GET':
		try:
			page = int(page)
		except:
			page = 1
		start = (page-1) * 2
		print(start)
		return render(request,'case_manage.html',{'type':'list','cases':contacts,'start':start})
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def search(request):
	'''用例搜索'''
	case_name = request.GET.get('case_name')
	cases = TestCase.objects.filter(name__contains=case_name)
	paginator = Paginator(cases,2)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)

	if request.method == 'GET':
		return render(request,'case_manage.html',{'type':'list','cases':contacts,'case_name':case_name})
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def case_add(request):
	'''用例调试界面'''
	return render(request,'case_add.html',{'type':'add'})

@login_required
def api_debug(request):
	'''新建并调试用例'''
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
		if name == '' or url == '':
			return HttpResponse('用例名称或请求url不能为空')
		else:
			TestCase.objects.create(name=name, url=url, method=method, params=params,headers=header, datatpye=datatpye)
			return HttpResponse('保存成功')

	else:
		return HttpResponse('请求方法错误')








