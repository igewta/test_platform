from django.db import models

# Create your models here.
class project(models.Model):
	'''
	项目表
	'''
	name = models.CharField('项目名称',max_length=50,blank=False,default='')
	description = models.TextField('项目描述',default='')
	status = models.BooleanField('状态',default=True)
	create_time = models.DateTimeField('创建时间',auto_now=True)

	def __str__(self):
		return self.name

class module(models.Model):
	'''
	模块表
	'''
	project = models.ForeignKey(project,on_delete=True)
	name = models.CharField('模块名称',max_length=50,default='')
	description = models.TextField('模块表述',default='')
	create_time = models.DateTimeField('创建时间',auto_now=True)

	def __str__(self):
		return self.name


