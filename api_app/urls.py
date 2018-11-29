from django.urls import path
from api_app.views import case_views
from api_app.views import case_api
from api_app.views import task_views


urlpatterns = [
	# cases_views
    path('', case_views.manage),
	path('add/', case_views.case_add),
	path('api_debug/',case_views.api_debug),
	path('search/',case_views.search),

	# cases_api
	path('caseslist/', case_api.cases_list),
	path('get_project_list/',case_api.get_project_list),
	
	# task_views
	path('task/', task_views.task_manage),
	path('task/add/', task_views.task_add),
]