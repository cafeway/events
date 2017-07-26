from django.shortcuts import render,render_to_response
from django.contrib.auth import  authenticate,login
# Create your views here.
def user(request):
    message='welcome'
    return  render_to_response('userpage.html',{'message':message})
def my_view(request):
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username,password=password)
	if user is not None:
		login(request,user)
	else:
		print('your are not authorised')

