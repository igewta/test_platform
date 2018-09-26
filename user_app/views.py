from django.shortcuts import render
from django.contrib import auth

# Create your views here.

def index(requests):
	return render(requests,'index.html')

def login_action(requests):
	if requests.method == "POST":
		username = requests.GET.get("username","")
		password = requests.GET.get("password","")

		if username == " " or password =="":
			return render(requests,"index.html",{'error':'用户名或者密码错误'})
		
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(requests,user)
			return render(requests,'project_manage.html',"登陆成功")
		else:
			return render(requests,'index.html',"用户名或密码错误")