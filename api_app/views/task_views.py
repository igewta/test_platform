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