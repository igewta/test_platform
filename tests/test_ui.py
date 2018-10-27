from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.select import Select
from django.contrib.auth.models import User
from project_app.models import project,module


class LoginTest(StaticLiveServerTestCase):
	'''登录测试 '''

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		cls.driver.get('%s%s' % (cls.live_server_url, '/'))

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		super().tearDownClass()

	def setUp(self):
		User.objects.create_user(username='test01',password='test123456',email='test01@mail.com')

	def tearDown(self):
		pass

	def test_01_login_null_user(self):
		'''测试登陆：用户名密码为空'''
		self.driver.find_element_by_name('username').send_keys('')
		self.driver.find_element_by_name('password').send_keys('')
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		tips = self.driver.find_element_by_xpath('//p').text
		self.assertEqual('用户名或者密码为空',tips)

	def test_02_login_error_user(self):
		'''测试登陆：用户名密码错误'''
		self.driver.find_element_by_name('username').send_keys('error')
		self.driver.find_element_by_name('password').send_keys('error')
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		tips = self.driver.find_element_by_xpath('//p').text
		self.assertEqual('用户名或者密码错误',tips)

	def test_03_login_success(self):
		'''测试登陆：登陆成功'''
		self.driver.find_element_by_name('username').send_keys('test01')
		self.driver.find_element_by_name('password').send_keys('test123456')
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		user = self.driver.find_element_by_xpath('//div[@id="navbar"]/ul/li[1]').text
		self.assertEqual('test01',user)


class ProjectTest(StaticLiveServerTestCase):
	'''项目管理测试'''

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.driver = webdriver.Chrome()

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		super().tearDownClass()

	def setUp(self):
		'''登录，初始化数据'''
		User.objects.create_user(username='test01',password='test123456',email='test01@mail.com')
		project.objects.create(name='project01',description='testproject01')
		self.driver.get('%s%s' % (self.live_server_url, '/manage/project/'))
		self.driver.find_element_by_name('username').send_keys('test01')
		self.driver.find_element_by_name('password').send_keys('test123456')
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		
	def tearDown(self):
		pass

	def test_01_project_list(self):
		'''测试 project 列表展示'''
		pro = self.driver.find_element_by_xpath('//table[@id="prlist"]/tbody/tr/td[2]').text
		self.assertEqual(pro,'project01')

	def test_02_add_project(self):
		'''测试添加 project '''
		self.driver.find_element_by_xpath('//button[contains(text(),"创建")]').click()
		self.driver.find_element_by_name('name').send_keys('project02')
		self.driver.find_element_by_name('description').send_keys('testproject02')
		self.driver.find_element_by_name('status').click()
		self.driver.find_element_by_xpath('//input[@type="submit"]').click()
		pro = self.driver.find_element_by_xpath('//table[@id="prlist"]/tbody/tr[2]/td[2]').text
		pro_d = self.driver.find_element_by_xpath('//table[@id="prlist"]/tbody/tr[2]/td[3]').text
		self.assertEqual('project02',pro)
		self.assertIn('testproject02',pro_d)

	def test_03_edit_project(self):
		'''测试编辑project'''
		self.driver.find_element_by_xpath('//td/a[contains(text(),"编辑")]').click()
		self.driver.find_element_by_name('name').clear()
		self.driver.find_element_by_name('name').send_keys('newproject01')
		self.driver.find_element_by_name('description').clear()
		self.driver.find_element_by_name('description').send_keys('newproject01description')
		self.driver.find_element_by_name('status').click()
		self.driver.find_element_by_xpath('//input[@type="submit"]').click()
		pro = self.driver.find_element_by_xpath('//table[@id="prlist"]/tbody/tr[1]/td[2]').text
		pro_d = self.driver.find_element_by_xpath('//table[@id="prlist"]/tbody/tr[1]/td[3]').text
		self.assertEqual('newproject01',pro)
		self.assertIn('newproject01description',pro_d)

	def test_04_del_project(self):
		'''测试删除project'''
		self.driver.find_element_by_xpath('//td/a[contains(text(),"删除")]').click()
		table = self.driver.find_element_by_id('prlist')
		pro = table.find_elements_by_xpath('tbody/tr')
		self.assertEqual(len(pro),0)


class ModuleTest(StaticLiveServerTestCase):
	'''项目管理测试'''

	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.driver = webdriver.Chrome()

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		super().tearDownClass()

	def setUp(self):
		'''登录，初始化数据'''
		User.objects.create_user(username='test01',password='test123456',email='test01@mail.com')
		project.objects.create(id=1,name='project01',description='testproject01')
		module.objects.create(project_id=1,name='module01',description='testmodule01')
		self.driver.get('%s%s' % (self.live_server_url, '/'))
		self.driver.find_element_by_name('username').send_keys('test01')
		self.driver.find_element_by_name('password').send_keys('test123456')
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		self.driver.find_element_by_link_text('模块管理').click()
		
	def tearDown(self):
		pass

	def test_01_module_list(self):
		'''测试 module 列表展示'''
		pro = self.driver.find_element_by_xpath('//table[@id="molist"]/tbody/tr/td[2]').text
		self.assertEqual(pro,'module01')

	def test_02_add_module(self):
		'''测试 添加 module '''
		self.driver.find_element_by_xpath('//button[contains(text(),"创建")]').click()
		sel = self.driver.find_element_by_name('project')
		Select(sel).select_by_value('1')
		self.driver.find_element_by_name('name').send_keys('module02')
		self.driver.find_element_by_name('description').send_keys('testmodule02')
		self.driver.find_element_by_xpath('//input[@type="submit"]').click()
		pro = self.driver.find_element_by_xpath('//table[@id="molist"]/tbody/tr[2]/td[2]').text
		pro_d = self.driver.find_element_by_xpath('//table[@id="molist"]/tbody/tr[2]/td[3]').text
		self.assertEqual('module02',pro)
		self.assertIn('testmodule02',pro_d)

	def test_03_edit_project(self):
		'''测试 编辑module'''
		self.driver.find_element_by_xpath('//td/a[contains(text(),"编辑")]').click()
		self.driver.find_element_by_name('name').clear()
		self.driver.find_element_by_name('name').send_keys('newmodule01')
		self.driver.find_element_by_name('description').clear()
		self.driver.find_element_by_name('description').send_keys('newmodule01description')
		self.driver.find_element_by_xpath('//input[@type="submit"]').click()
		pro = self.driver.find_element_by_xpath('//table[@id="molist"]/tbody/tr[1]/td[2]').text
		pro_d = self.driver.find_element_by_xpath('//table[@id="molist"]/tbody/tr[1]/td[3]').text
		self.assertEqual('newmodule01',pro)
		self.assertIn('newmodule01description',pro_d)

	def test_04_del_module(self):
		'''测试删除module'''
		self.driver.find_element_by_xpath('//td/a[contains(text(),"删除")]').click()
		table = self.driver.find_element_by_id('molist')
		pro = table.find_elements_by_xpath('tbody/tr')
		self.assertEqual(len(pro),0)



