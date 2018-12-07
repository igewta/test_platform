import requests
from test_platform.common import resp_success,resp_fail
from django.contrib.auth.decorators import login_required
from api_app.models import TestCase,TestTask
from project_app.models import project,module


@login_required
def task_save(request):
	'''保存任务'''
	if request.method == 'POST':
		task_name = request.POST.get('task_name','')
		task_describe = request.POST.get('task_describe','')
		task_status = request.POST.get('task_status','0')
		task_cases = request.POST.get('task_cases','')
		if task_name == '' or task_cases == '':
			return resp_fail('任务名称和用例不能为空')
		else:
			task = TestTask.objects.create(name=task_name, describe=task_describe, status=task_status, cases=task_cases)
			if task:
				return resp_success(message='保存成功')
			else:
				return resp_fail(message='保存失败')

@login_required
def task_update(request,tid):
	'''更新任务'''
	if request.method == 'POST':
		task_name = request.POST.get('task_name','')
		task_describe = request.POST.get('task_describe','')
		task_status = request.POST.get('task_status','0')
		task_cases = request.POST.get('task_cases','')
		if task_name == '' or task_cases == '':
			return resp_fail('任务名称和用例不能为空')
		else:
			task = TestTask.objects.get(id=tid)
			task.name = task_name 
			task.describe = task_describe 
			task.status = task_status 
			task.cases = task_cases
			task.save()
			if task:
				return resp_success(message='保存成功')
			else:
				return resp_fail(message='保存失败')
	else:
		return resp_fail('请求方法错误')

@login_required
def task_info(request):
	'''任务具体信息'''
	if request.method == 'GET':
		tid = request.GET.get('tid','')
		if tid == '':
			return resp_fail('任务id不存在')
		try:
			task_obj = TestTask.objects.get(id=tid)
		except:
			resp_fail('任务id不存在')
		else:
			task_info = {
			'id':tid,
			'name':task_obj.name,
			'describe':task_obj.describe,
			'status':task_obj.status,
			'cases':task_obj.cases
			}

			return resp_success(data=task_info)

	else:
		return resp_fail('请求方法有误')
