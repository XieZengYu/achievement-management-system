from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django import forms
from django.contrib import auth
from user_management.models import *
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# Create your views here.

# Form
class UserForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

def login(request):
	sign = 4
	if request.method == 'POST':
		username = request.POST.get('Userame')
		password = request.POST.get('Password')
		print(username)
		print('========================================')
		user_s = Student.objects.filter(account = username,password = password).first()
		print(user_s)
		print('========================================')
		if user_s is None:
			user_t = Teacher.objects.filter(account = username,password = password).first()
			if user_t is None:
				print(user_t)
				print('========================================')
				user = auth.authenticate(username=username,password=password)
				if user is not None and user.is_active:
					auth.login(request,user)
					#sign = 3
					request.session['sign'] = 3
					request.session['account'] = username
					request.session['uname'] = username
					request.session['login'] = True
					request.session['u_id'] = username
					#return render_to_response('index.html',{'account':username,'sign':sign})
					return HttpResponseRedirect('/index/')
				else:
					sign = 0
					return render_to_response('login.html',{'pwd_wrong':True})
			else:
				uname = Teacher.objects.filter(account = username).first().name
				#sign = 2
				request.session['sign'] = 2
				request.session['uname'] = uname
				request.session['account'] = username
				request.session['login'] = True
				request.session['u_id'] = Teacher.objects.filter(account = username).first().id
				print('========================================')
				print(request.session['u_id'])
				print(request.session['uname'])
				print(request.session['account'])
				print(type(request.session['u_id']))
				print('========================================')
				#return render_to_response('index.html',{'account':username,'sign':sign,'uname':uname})
				return HttpResponseRedirect('/index/')
		else:
			uname = Student.objects.filter(account = username).first().name
			request.session['sign'] = 1
			request.session['uname'] = uname
			request.session['account'] = username
			request.session['login'] = True
			request.session['u_id'] = Student.objects.filter(account = username).first().id
			print(request.session['u_id'])
			#sign = 1
			return HttpResponseRedirect('/index/')
			#return render_to_response('index.html',{'account':username,'sign':sign,'uname':uname})
		#print( sign )
	return render_to_response('login.html')


def index(request):
	print('========================================')
	is_login = request.session.get('login',False)
	print('========================================')
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]
		uname = request.session["uname"]
		u_id = request.session['u_id']

		print('========================================')
		print(sign)
		print(username)
		print(uname)
		print(u_id)
		print(type(u_id))
		print('========================================')
		campus_list = CampusInfo.objects.all()
		paginator = Paginator(campus_list,8)
		try:
			page = int(request.GET.get('page', '1'))
		except ValueError:
			page = 1
		try:
			contacts = paginator.page(page)
		except (EmptyPage, InvalidPage):
			contacts = paginator.page(paginator.num_pages)
		print('=--------------------========================')
		print(contacts)
		print('---------------------------=================')
		return render_to_response('index.html', {"contacts": contacts,'account':username,'sign':sign,'u_id':u_id,'uname':uname})
	else:
		return HttpResponseRedirect('/login/')

def news(request, offset):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]		
		uname = request.session["uname"]
		u_id = request.session['u_id']
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		news_list = CampusInfo.objects.get(id=offset)
		
		#return render_to_response('/news/%d'%offset,{'news_list':news_list})
		return render_to_response('news.html',{'news_list':news_list,'account':username,'sign':sign,'uname':uname,'u_id':u_id,})
	else:
		return HttpResponseRedirect('/login/')


# 	Change Password Form
class ChangePasswordForm(forms.Form):
	old_pwd = forms.CharField()
	new_pwd = forms.CharField()
	con_pwd = forms.CharField()


def ChangePassword(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]
		uname = request.session["uname"]
		u_id = request.session["u_id"]
		old_e = False
		new_e = False
		suc = False
		if request.method == 'POST':
			pwd = ChangePasswordForm(request.POST)
			if pwd.is_valid():
				old_pwd = pwd.cleaned_data['old_pwd']
				new_pwd = pwd.cleaned_data['new_pwd']
				con_pwd = pwd.cleaned_data['con_pwd']
				print('========================================')
				print(old_pwd)
				print(new_pwd)
				print(con_pwd)
				print('========================================')
				if sign == 1:
					#Student
					if new_pwd == con_pwd:
						s_p = Student.objects.filter(account = username,password = old_pwd)
						print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
						print(s_p)
						print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
						if s_p:
							s_p.update(password=new_pwd)
							suc = True
							return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
						else:
							#the old_password is error
							old_e = True
							return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
					else:
						#the new_password is different with the comfirm_password
						new_e = True
						return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
				else:
					#Teacher
					if new_pwd == con_pwd:
						t_p = Teacher.objects.filter(account = username,password = old_pwd)
						print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
						print(t_p)
						print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
						if t_p:
							t_p.update(password=new_pwd)
							suc = True
							return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
						else:
							#the old_password is error
							old_e = True
							return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
					else:
						#the new_password is different with the comfirm_password
						new_e = True
						return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
		else:
			pwd = ChangePasswordForm()
			return render_to_response('changepwd.html',{'old_e':old_e,'new_e':new_e,'suc':suc,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
	else:
		return HttpResponseRedirect('/login/')
