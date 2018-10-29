from django.test import TestCase
from django.contrib.auth.models import User
from project_app.models import project,module


class UserModelTest(TestCase):
	'''
	User model 测试
	'''
	def setUp(self):
		'''初始化数据'''
		User.objects.create_user('test01','test01@mail.com','test123456')

	def tearDown(self):
		pass

	def test_01_add(self):
		'''测试新增用户'''
		User.objects.create_user('test02','test02@mail.com','test123456')
		user = User.objects.get(username="test02")
		self.assertEqual(user.email,'test02@mail.com')

	def test_02_get(self):
		'''测试查询用户'''
		user = User.objects.get(username='test01')
		self.assertEqual(user.email,'test01@mail.com')

	def test_03_update(self):
		'''测试更新用户'''
		user = User.objects.get(username='test01')
		user.email = 'newtest01@mail.com'
		user.save()
		self.assertEqual(user.email,'newtest01@mail.com')

	def test_04_del(self):
		'''测试删除用户'''
		User.objects.get(username='test01').delete()
		user = User.objects.filter(username='test01')
		self.assertEqual(len(user),0)


class ProjectModelTest(TestCase):
	'''
	project model 测试
	'''
	def setUp(self):
		'''初始化数据'''
		project.objects.create(name="testproject01",description='description01')
	
	def tearDown(self):
		pass

	def test_01_add(self):
		'''测试增加项目'''	
		project.objects.create(name='testproject02',description='descriptin02')
		pro = project.objects.get(name='testproject02')
		self.assertEqual(pro.description,'descriptin02')

	def test_02_get(self):
		'''测试查询项目'''
		pro = project.objects.get(name='testproject01')
		self.assertEqual(pro.description,'description01')

	def test_03_update(self):
		'''测试更新项目'''
		pro = project.objects.get(name='testproject01')
		pro.description = 'newdescription'
		pro.save()
		self.assertEqual(pro.description,'newdescription')

	def test_04_del(self):
		'''测试删除项目'''
		project.objects.get(name='testproject01').delete()
		pro = project.objects.filter(name='testproject01')
		self.assertEqual(len(pro),0)


class ModuleModelTest(TestCase):
	'''
	module model 测试
	'''
	def setUp(self):
		'''初始化数据'''
		project.objects.create(name='project01',description='testproject01')
		module.objects.create(project_id=1,name='module01',description='testmodule01')

	def tearDown(self):
		pass

	def test_01_add(self):
		'''测试添加模块'''
		project.objects.create(name='project02',description='testproject02')
		module.objects.create(project_id=2,name='module02',description='testmodule02')
		mod = module.objects.get(name='module02')
		self.assertEqual(mod.description,'testmodule02')

	def test_02_get(self):
		'''测试查询模块'''
		mod = module.objects.get(name='module01')
		self.assertEqual(mod.description,'testmodule01')

	def test_03_upate(self):
		'''测试更新模块'''
		mod = module.objects.get(name='module01')
		mod.description = 'newdescription'
		mod.save()
		self.assertEqual(mod.description,'newdescription')

	def test_04_del(self):
		'''测试删除模块'''	
		module.objects.get(name='module01').delete()
		mod = module.objects.filter(name='module01')
		self.assertEqual(len(mod),0)

