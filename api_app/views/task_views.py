import requests
import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from api_app.models import TestCase,TestTask
from project_app.models import project,module


'''
有关任务的界面显示、操作等
'''

# 任务管理页
@login_required
def task_manage(request):
	if request.method == 'GET':
		tasks = TestTask.objects.all()
		return render(request,'api_app/task_manage.html',{'type':'list','tasks':tasks})
	else:
		return HttpResponse('404 NOT FOUND')

# 任务添加页
@login_required
def task_add(request):
	if request.method == 'GET':
		return render(request,'api_app/task_add.html',{'type':'add'})
	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def task_edit(request,tid):
	'''任务编辑界面'''
	task_obj = TestTask.objects.get(id=tid)
	return render(request,'api_app/task_edit.html',{'type':'edit','task_obj':task_obj})

@login_required
def task_del(request,tid):
	'''删除任务''' 
	TestTask.objects.get(id=tid).delete()
	return HttpResponseRedirect('/cases/task/')

@login_required
def task_run(request,tid):
	'''运行任务'''
	if request.method == 'GET':
		task_obj = TestTask.objects.get(id=tid)
		return HttpResponseRedirect('/cases/task/')
	else:
		return HttpResponse('404 NOT FOUND')