from django.urls import path
from project_app.views import project_views,module_views

urlpatterns = [
    path('project/', project_views.project_manage),
    path('project/add/',project_views.add_project),
    path('project/edit/<int:pid>/',project_views.edit_project),
    path("project/del/<int:pid>/",project_views.del_project),

    path('module/', module_views.module_manage),
    path('module/add/',module_views.add_module),
    path('module/edit/<int:mid>/',module_views.edit_module),
    path('module/del/<int:mid>/',module_views.del_module),

    ]