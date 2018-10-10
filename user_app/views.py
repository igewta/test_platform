from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from user_app.models import project,module


# Create your views here.

def index(requests):
	return render(requests,'index.html')

def login_action(requests):
	if requests.method == "POST":
		username = requests.POST.get("username"," ")
		password = requests.POST.get("password"," ")

		if username == "" or password =="":
			return render(requests,"index.html",{'error':'用户名或者密码为空'})
		
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(requests,user)
			requests.session['user'] = username
			response = HttpResponseRedirect('/project_manage/')
			# response.set_cookie('user',username)
			return response
		else:
			return render(requests,'index.html',{'error':'用户名或者密码错误'})

	else:
		return render(requests,'index.html')
		
def logout(requests):
	auth.logout(requests)
	return HttpResponseRedirect('/index/')

@login_required
def project_manage(requests):
	# username = requests.COOKIES.get('user')
	username = requests.session.get('user','')
	project_all = project.objects.all()
	print(project_all)
	return render(requests,'project_manage.html',
							{'user':username,
							'projects':project_all}
							)


@login_required
def module_manage(requests):
	username = requests.session.get('user','')
	module_all = module.objects.all()
	return render(requests,'module_manage.html',
							{'user':username,
							'modules':module_all}
							)









def project_create(requests):
	return render(requests,'project_create.html')

def project_save(requests):
	if requests.method == 'POST':
		projectname = requests.POST.get('projectname','')
		description = requests.POST.get('description','')

		if projectname == '' or description =='':
			return render(requests,'project_create.html',{'error':'项目名称或项目描述不能为空'})
		else:

			return HttpResponseRedirect('/project_manage/')

	else:
		return render(requests,'project_create.html',{'error':'请求方法错误，请使用POST方法'})





		