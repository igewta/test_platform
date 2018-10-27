from django.test import TestCase,Client
from django.contrib.auth.models import User
from project_app.models import project,module


class UserAppTest(TestCase):
	'''user_app.views 测试'''
	
	def setUp(self):
		'''初始化数据'''
		User.objects.create_user(username='test01',email='test01@mail.com',password='test123456')
		self.client = Client()

	def tearDown(self):
		pass

	def test_01_index(self):
		'''测试 index 函数'''
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'index.html')

	def test_02_login_action_get(self):
		'''测试 login_action 函数 get 方法'''
		response = self.client.get('/login_action/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'index.html')

	def test_03_login_action_user_null(self):
		'''测试 login_action post:用户名密码为空'''
		response = self.client.post('/login_action/',data = {'username':'','password':''})
		self.assertEqual(response.status_code,200)
		self.assertIn('用户名或者密码为空',response.content.decode('utf-8'))
	def test_04_login_action_user_error(self):
		'''测试 login_action post:用户名密码错误'''
		response = self.client.post('/login_action/',data = {'username':'error','password':'error'})
		self.assertEqual(response.status_code,200)
		self.assertIn('用户名或者密码错误',response.content.decode('utf-8'))

	def test_05_login_action_success(self):
		'''测试 login_action post:用户登陆成功'''
		response = self.client.post('/login_action/',data = {'username':'test01','password':'test123456'})
		self.assertEqual(response.status_code,302)

	def test_06_logout(self):
		self.client.post('/login_action/',data = {'username':'test01','password':'test123456'})
		response = self.client.get('/logout/')
		self.assertEqual(response.status_code,302)


class ProjectAppProjectTest(TestCase):
	'''project_app.views.project_views 测试'''

	def setUp(self):
		'''初始化数据，登陆'''
		User.objects.create_user(username='test01',email='test01@mail.com',password='test123456')
		project.objects.create(name='project01',description='testproject01')
		self.client = Client()
		self.client.post('/login_action/',data={'username':'test01','password':'test123456'})

	def tearDown(self):
		pass

	def test_01_project_manage(self):
		'''测试 project_manage:展示列表数据'''
		response = self.client.get('/manage/project/')
		self.assertTemplateUsed(response,'project.html')
		self.assertIn('project01',response.content.decode('utf-8'))

	def test_02_add_project_get(self):
		'''测试 add_project get:添加项目界面'''
		response = self.client.get('/manage/project/add/')
		self.assertIn('项目描述',response.content.decode('utf-8'))
		self.assertTemplateUsed(response,'project.html')

	def test_03_add_project_success(self):
		'''测试 add_project post:添加项目'''
		response = self.client.post('/manage/project/add/',data={'name':'project02','description':'test02description'})
		self.assertEqual(response.status_code,302)
		pro = project.objects.filter(name='project02')
		self.assertEqual(len(pro),1)

	def test_04_edit_project_get(self):
		'''测试 edit_project get:编辑项目界面'''
		response = self.client.get('/manage/project/edit/1/')
		self.assertEqual(response.status_code,200)
		self.assertIn('testproject01',response.content.decode('utf-8'))

	def test_05_edit_project_sucess(self):
		'''测试 edit_project post:编辑项目'''
		response = self.client.post('/manage/project/edit/1/',data={'name':"newtest01",'description':'newdescription'})
		self.assertEqual(response.status_code,302)
		pro = project.objects.get(name='newtest01')
		self.assertEqual(pro.description,'newdescription')

	def test_06_del_project(self):
		'''测试 del_project:删除项目'''
		self.client.get('/manage/project/del/1/')
		pro = project.objects.filter(id=1)
		self.assertEqual(len(pro),0)


class ProjectAppModuleTest(TestCase):
	''' project_app.views.module_views 测试'''

	def setUp(self):
		'''数据初始化，登陆'''
		User.objects.create_user(username='test01',email='test01@mail.com',password='test123456')
		project.objects.create(id=1,name='project01',description='testproject01')
		module.objects.create(project_id=1,name='module01',description='testmodule01')
		self.client = Client()
		self.client.post('/login_action/',data={'username':'test01','password':'test123456'})

	def tearDown(self):
		pass

	def test_01_module_manage(self):
		'''测试 module_manage:展示列表数据'''
		response = self.client.get('/manage/module/')
		self.assertTemplateUsed(response,'module.html')
		self.assertIn('module01',response.content.decode('utf-8'))

	def test_02_add_project_get(self):
		'''测试 add_module get:添加模块界面'''
		response = self.client.get('/manage/module/add/')
		self.assertIn('模块表述',response.content.decode('utf-8'))
		self.assertTemplateUsed(response,'module.html')

	def test_03_add_module_success(self):
		'''测试 add_module post:添加模块'''
		response = self.client.post('/manage/module/add/',data={'project':1,'name':'module02','description':'test02description'})
		self.assertEqual(response.status_code,302)
		mod = module.objects.filter(name='module02')
		self.assertEqual(len(mod),1)

	def test_04_edit_module_get(self):
		'''测试 edit_module get:编辑模块界面'''
		response = self.client.get('/manage/module/edit/1/')
		self.assertEqual(response.status_code,200)
		self.assertIn('testmodule01',response.content.decode('utf-8'))

	def test_05_edit_module_sucess(self):
		'''测试 edit_module post:编辑模块'''
		response = self.client.post('/manage/module/edit/1/',data={'project':1,'name':"newtest01",'description':'newdescription'})
		self.assertEqual(response.status_code,302)
		pro = module.objects.get(name='newtest01')
		self.assertEqual(pro.description,'newdescription')
	
	def test_06_del_module(self):
		'''测试 del_module:删除模块'''
		response = self.client.get('/manage/module/del/1/')
		mod = module.objects.filter(id=1)
		self.assertEqual(len(mod),0)
		self.assertEqual(response.status_code,302)
