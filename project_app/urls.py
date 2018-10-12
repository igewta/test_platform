from django.urls import path
from project_app import views

urlpatterns = [
    path('manage/', views.project_manage),
    path('add/',views.add_project),
    ]