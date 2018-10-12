from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from project_app.models import project,module


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
			response = HttpResponseRedirect('/project/manage/')
			# response.set_cookie('user',username)
			return response
		else:
			return render(requests,'index.html',{'error':'用户名或者密码错误'})

	else:
		return render(requests,'index.html')
		
def logout(requests):
	auth.logout(requests)
	return HttpResponseRedirect('/index/')


