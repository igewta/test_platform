from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import project

# Create your views here.
@login_required
def project_manage(requests):
	# username = requests.COOKIES.get('user')
	username = requests.session.get('user','')
	project_all = project.objects.all()
	print(project_all)
	return render(requests,'project_manage.html',
					{'user':username,'projects':project_all,'type':'list'}
				)

@login_required
def add_project(requests):
	return render(requests,'project_manage.html',{'type':'add'})

