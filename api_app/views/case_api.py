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
