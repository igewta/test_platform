from django.urls import path
from api_app.views import case_views
from api_app.views import case_api
from api_app.views import task_views
from api_app.views import task_api

urlpatterns = [
	# cases_views
    path('', case_views.manage),
	path('add/', case_views.case_add),
	path('search/',case_views.search),
	path('edit/<int:cid>/',case_views.edit),
	path('delete/<int:cid>/',case_views.delete),

	# cases_api
	path('caseslist/', case_api.cases_list),
	path('cases_info/',case_api.cases_info),
	path('get_project_list/',case_api.get_project_list),
	path('api_debug/',case_api.api_debug),
	path('case_assert/',case_api.case_assert),
	path('save/',case_api.save),
	path('update/',case_api.update),
	
	# task_views
	path('task/', task_views.task_manage),
	path('task/add/', task_views.task_add),
	path('task/edit/<int:tid>/',task_views.task_edit),
	path('task/del/<int:tid>/',task_views.task_del),
	path('task/run/<int:tid>/',task_views.task_run),

	# task_api
	path('task/save/',task_api.task_save),
	path('task/update/',task_api.task_update),
	path('task_info/',task_api.task_info),
]