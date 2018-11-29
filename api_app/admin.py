from django.contrib import admin
from api_app.models import TestCase,TestTask

class TestCaseAdmin(admin.ModelAdmin):
	lis_display = ['name','descripe','status','cases']


class TestTaskAdmin(admin.ModelAdmin):
	lis_display = ['name','descripe','status','cases']

admin.site.register(TestCase,TestCaseAdmin)
admin.site.register(TestTask,TestTaskAdmin)