from django.shortcuts import render

# Create your views here.

def index(requests):
	return render(requests,'index.html')

def login_action(requests):
	if requests.method == "GET":
		username = requests.GET.get("username")
		password = requests.GET.get("password")

		if username == " " or password =="":
			return render(requests,"index.html",{'error':'用户名或者密码错误'})
			
