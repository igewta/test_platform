from django.urls import path
from project_app import views

urlpatterns = [
    path('manage/', views.project_manage),
    path('add/',views.add_project),
    path('edit/<int:pid>/',views.edit_project),
    path('del/<int:pid>/',views.del_project),
    ]