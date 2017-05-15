from django.shortcuts import render
from admin_operation.forms import UserImportForm,CampusInfoForm
from teacher_operation.forms import *
from admin_operation.models import UserImport
from django import forms
from user_management.models import *
from CourseAndScore.models import *
from django.views.generic.edit import UpdateView
# Create your views here.

class TeacherUpdate(UpdateView):
	model = Teacher
	fields = ['gender','department','phone_num','address']
	template_name_suffix  =  '_update'
	success_url = '/index/'

	def get_context_data(self,**kwargs):
		# import pdb; pdb.set_trace();
		context = super(UpdateView,self).get_context_data(**kwargs)
		context['sign'] =self.request.session["sign"]
		context['username'] = self.request.session["account"]
		context['uname'] = self.request.session["uname"]
		context['u_id'] = self.request.session["u_id"]
		return context

	def get(self, request, *args, **kwargs):
		is_login = request.session.get('login',False)
		print(is_login)
		print('________________________________________')
		if is_login:
			return super().get(self, request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/login/')