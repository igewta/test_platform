from django.db import models
from project_app.models import module

# Create your models here.
class case(models.Model):
	'''用例表'''
	module = models.ForeignKey(module,on_delete=models.CASCADE)
	name = models.CharField('用例名称', max_length=50, blank=False, default='')
	url = models.CharField('请求url', max_length=100,default='')
	method = models.CharField('请求方法',max_length=10, default='')
	params = models.TextField('请求参数',default='{}')
	header = models.TextField('请求头部',default='{}')
	respose =  models.TextField('返回结果',default='')
	create_time = models.DateTimeField('创建时间',auto_now=True)

	def __str__(self):
		return self.name