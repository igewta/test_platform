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

# 获取用例列表
@login_required
def cases_list(request):
	porjects = project.objects.all()
	cases_list = []

	if request.method == 'GET':
		for project in projects:
			modules = module.objects.filter(project_id=project.id)
			for module in modules:
				cases = TestCase.objects.filter(module_id=module.id)
				if len(cases) !=0:
					for case in cases:
						case_info = project.name + '-->' + module.name + "-->" + case.name
						cases_list.append(case_info)
				else:
					pass
		data = {'caseslist':cases_list}
		return JsonResponse(data)

	else:
		return HttpResponse('404 NOT FOUND')
