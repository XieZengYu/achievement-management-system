from django.shortcuts import render,render_to_response
from django.http import HttpResponse

# Create your views here.
def base(request):
	return render_to_response('base.html')

def base1(request):
	return render_to_response('base1.html')

def login(request):
	return render_to_response('login.html')
