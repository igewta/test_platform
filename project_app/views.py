from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import project
from project_app.forms import projectForm


# Create your views here.
@login_required
def project_manage(requests):
	# username = requests.COOKIES.get('user')
	username = requests.session.get('user','')
	project_all = project.objects.all()
	print(project_all)
	return render(requests,'project_manage.html',{'user':username,'projects':project_all,'type':'list'})


@login_required
def add_project(requests):
	if requests.method == "POST":
		form = projectForm(requests.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']
			project.objects.create(name=name,description=description,status=status)
			return HttpResponseRedirect('/project/manage/')			
	else:
		form = projectForm()
	return render(requests,'project_manage.html',{"form":form,'type':'add'})


@login_required
def edit_project(requests,pid):
	id = pid
	ob = project.objects.get(id=pid)

	if requests.method == 'POST':
		form = projectForm(requests.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			status = form.cleaned_data['status']
			ob.name = name
			ob.description = description
			ob.status = status
			ob.save()
			return HttpResponseRedirect('/project/manage/')
	else:		
		name = ob.name
		description = ob.description
		status = ob.status
		form = projectForm(initial={'name': name,'description':description,'status':status})
		return render(requests,'project_manage.html',{'form':form,'pid':id,'type':'edit'})


@login_required
def del_project(requests,pid):
	id = pid
	project.objects.get(id=id).delete()
	return HttpResponseRedirect('/project/manage/')
