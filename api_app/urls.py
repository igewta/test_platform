from django.urls import path
from api_app.views import case_views
from api_app.views import case_api
from api_app.views import task_views


urlpatterns = [
	# cases_views
    path('', case_views.manage),
	path('debug/', case_views.debug),
	path('api_debug/',case_views.api_debug),
	path('save/',case_views.save),

	# cases_api
	path('caseslist/', case_api.cases_list),
	
	# task_views
	path('task/', task_views.task_manage),
	path('task/add/', task_views.task_add),
]