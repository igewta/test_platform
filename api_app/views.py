from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def manage(request):
	return render(request,'cases.html',{'type':'list'})

@login_required
def debug(request):
	return render(request,'debug.html',{'type':'debug'})