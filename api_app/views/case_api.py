import requests
from test_platform.common import resp_success,resp_fail
from django.contrib.auth.decorators import login_required
from api_app.models import TestCase
from project_app.models import project,module

'''
有关用例的接口
'''

@login_required
def get_project_list(request):
	'''获取：项目-模块二级联动信息：返回项目/模块 id 和名称'''
	if request.method == 'GET':
		projects = project.objects.all()
		datalist = []
		for p in projects:
			project_dict = {'pid':p.id,'p_name': p.name }
			modules = module.objects.filter(project_id=p.id)
			module_name = []
			if len(modules) != 0:
				for m in modules:
					m_info = {'mid':m.id,'m_name':m.name}
					module_name.append(m_info)
			project_dict['moduleList'] = module_name
			datalist.append(project_dict)
		return resp_success(data=datalist)

	else:
		return HttpResponse('404 NOT FOUND')

@login_required
def cases_list(request):
	'''获取所有用例列表'''
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
		return resp_success(data=data)

	else:
		return resp_fail('404 NOT FOUND')

def cases_info(request):
	'''获取用例信息'''
	if request.method == 'POST':
		cid = request.POST.get('caseid','')
		if cid == '':
			return resp_fail('用例id不存在')

		try:
			case = TestCase.objects.get(id=cid)
		except:
			return resp_fail('用例id不存在')

		module_obj = module.objects.get(id=case.module_id)
		case_info = {
		'name' :case.name,
		'url':case.url,
		'method' :case.method,
		'datatpye' :case.datatpye,
		'headers' : case.headers,
		'params' : case.params,
		'result' : case.result,
		'module_id' : case.module_id,
		'project_id' : module_obj.project_id,
		}
		return resp_success(data=case_info)
	else:
		return resp_fail('404 NOT FOUND')

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
			return resp_fail(f'url:{url} 的格式不正确')

		if params != '':
			try:
				data = json.loads(params.replace("'", "\""))
			except :
				return resp_fail(f'参数：{params} 不是dict 格式')

		if header != '':
			try:
				head_json = json.loads(header.replace("'","\""))
			except :
				return resp_fail(f'header：{header} 不是dict 格式')

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
		data = r.content.decode('utf-8')
		return resp_success(data=data)
	else:
		return resp_fail('404 NOT FOUND')

@login_required
def case_assert(request):
	'''用例断言'''
	if request.method == 'POST':
		case_resp = request.POST.get('case_resp','')
		case_assert = request.POST.get('case_assert','')
		if case_assert in case_resp:
			return resp_success(data='断言成功')
		else:
			return resp_fail('断言失败')
	else:
		return resp_fail('请求方法错误')

@login_required
def save(request):
	'''保存测试用例''' 
	if request.method == 'POST':
		name = request.POST.get('name','')
		url = request.POST.get("url",'')
		method = request.POST.get('method','get')
		params = request.POST.get('params','form')
		header = request.POST.get('header','')
		datatype = request.POST.get("datatype",'')
		module_id = request.POST.get('module_id','')
		project_id = request.POST.get('project_id','')
		assert_text = request.POST.get('assert_text','')

		if name == '' or url == '' or module_id == '' or project_id == '' or assert_text == '':
			return resp_fail('name,url,模块，项目，断言：参数不能为空，请检查')
		else:
			module_obj = module.objects.get(id=module_id)
			project_obj =project.objects.get(id=module_obj.project_id)
			case = TestCase.objects.create(project_name=project_obj.name,module_id=module_id,name=name, url=url, method=method, params=params,headers=header, datatpye=datatype,result=assert_text)
			if case:
				return resp_success(data='保存成功')
			else:
				return resp_fail('保存失败，请重新尝试')
	else:
		return resp_fail('请求方法错误')

@login_required
def update(request):
	'''编辑更新测试用例''' 
	if request.method == 'POST':
		cid = request.POST.get('caseid','')
		name = request.POST.get('name','')
		url = request.POST.get("url",'')
		method = request.POST.get('method','get')
		params = request.POST.get('params','form')
		header = request.POST.get('header','')
		datatype = request.POST.get("datatype",'')
		module_id = request.POST.get('module_id','')
		project_id = request.POST.get('project_id','')
		assert_text = request.POST.get('assert_text','')

		if name == '' or url == '' or module_id == '' or project_id == '' or assert_text == '':
			return resp_fail('name,url,模块，项目，断言：参数不能为空，请检查')
		else:
			module_obj = module.objects.get(id=module_id)
			project_obj =project.objects.get(id=module_obj.project_id)
			case = TestCase.objects.get(id=cid)
			case.project_name=project_obj.name
			case.module_id=module_id
			case.name=name
			case.url=url
			case.method=method
			case.params=params
			case.headers=header
			case.datatpye=datatype
			case.result=assert_text
			case.save()
			if case:
				return resp_success(data='更新成功')
			else:
				return resp_fail('更新失败，请重新尝试')
	else:
		return resp_fail('请求方法错误')



