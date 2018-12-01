import requests
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from api_app.models import TestCase
from project_app.models import project,module
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''
有关用例的界面显示、操作等
'''

@login_required
def manage(request):
	'''用例管理列表'''
	cases = TestCase.objects.all()
	paginator = Paginator(cases,20)

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
		start = (page-1) * 20
		return render(request,'api_app/case_manage.html',{'type':'list','cases':contacts,'start':start})
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def search(request):
	'''用例搜索'''
	case_name = request.GET.get('case_name')
	cases = TestCase.objects.filter(name__contains=case_name)
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
		return render(request,'api_app/case_manage.html',{'type':'list','cases':contacts,'case_name':case_name,'start':start})
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def case_add(request):
	'''用例添加界面'''
	return render(request,'api_app/case_add.html',{'type':'add'})

@login_required
def edit(request,cid):
	'''用例编辑界面'''
	return render(request,'api_app/case_edit.html',{'type':'edit','cid':cid})

@login_required
def delete(request,cid):
	'''删除测试用例''' 
	TestCase.objects.get(id=cid).delete()
	return HttpResponseRedirect('/cases/')







