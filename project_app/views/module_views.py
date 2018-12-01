from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import module
from project_app.forms import moduleForm


# Create your views here.
@login_required
def module_manage(requests):
	# username = requests.COOKIES.get('user')
	username = requests.session.get('user','')
	module_all = module.objects.all()
	return render(requests,'project_app/module.html',{'user':username,'modules':module_all,'type':'list'})


@login_required
def add_module(requests):
	if requests.method == "POST":
		form = moduleForm(requests.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			project = form.cleaned_data['project']
			module.objects.create(name=name,description=description,project=project)
			return HttpResponseRedirect('/manage/module/')			
	else:
		form = moduleForm()
	return render(requests,'project_app/module.html',{"form":form,'type':'add'})


@login_required
def edit_module(requests,mid):
	ob = module.objects.get(id=mid)
	if requests.method == 'POST':
		form = moduleForm(requests.POST)
		if form.is_valid():
			ob.name = form.cleaned_data['name']
			ob.description = form.cleaned_data['description']
			ob.project = form.cleaned_data['project']
			ob.save()
			return HttpResponseRedirect('/manage/module/')
	else:
		form = moduleForm(instance=ob)
		return render(requests,'project_app/module.html',{'form':form,'mid':mid,'type':'edit'})

@login_required
def del_module(requests,mid):
	module.objects.get(id=mid).delete()
	return HttpResponseRedirect('/manage/module/')
