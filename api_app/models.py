from django.db import models

# Create your models here.
class TestCase(models.Model):
	'''
	测试用例表
	'''
	name = models.CharField('用例名称', max_length=100, blank=False, default='')
	url = models.TextField('url地址', default='')
	method = models.CharField('请求方法', max_length=10, default='get')
	datatpye = models.CharField('参数形式', max_length=10, default='form')
	headers = models.TextField('请求header', default='')
	params = models.TextField('请求参数',default='')
	create_time = models.DateTimeField('创建时间', auto_now=True)


