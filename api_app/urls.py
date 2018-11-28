from django.urls import path
from api_app.views import api_views

urlpatterns = [
    path('', api_views.manage),
	path('debug/', api_views.debug),
	path('api_debug/',api_views.api_debug),
	path('save/',api_views.save),

]