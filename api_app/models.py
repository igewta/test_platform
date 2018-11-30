from django.db import models
from project_app.models import module

# Create your models here.
class TestCase(models.Model):
	'''
	测试用例表
	'''
	module = models.ForeignKey(module, on_delete=models.CASCADE)
	project_name = models.CharField('所属项目', max_length=50, default='')
	name = models.CharField('用例名称', max_length=100, blank=False, default='')
	url = models.TextField('url地址', default='')
	method = models.CharField('请求方法', max_length=10, default='get')
	datatpye = models.CharField('参数形式', max_length=10, default='form')
	headers = models.TextField('请求header',default='')
	params = models.TextField('请求参数',default='')
	result = models.TextField('返回结果',default='')
	create_time = models.DateTimeField('创建时间', auto_now=True)

	def __str__(self):
		return self.name


class TestTask(models.Model):
	'''
	任务表
	'''
	name = models.CharField('任务名称', max_length=100, blank=False, default='')
	describe = models.TextField('任务描述', default='')
	status = models.IntegerField('状态', default=0) # 0 未运行，1 运行中，2 已运行
	cases = models.TextField('包含用例', default='')
	create_time = models.DateTimeField('创建时间', auto_now=True)

	def __str__(self):
		return self.name
