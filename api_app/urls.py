from django.urls import path
from api_app import views

urlpatterns = [
    path('', views.manage),
	path('debug/', views.debug),
	path('api_debug/',views.api_debug),
	path('save/',views.save),

]