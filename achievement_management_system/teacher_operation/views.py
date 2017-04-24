from django.shortcuts import render,render_to_response
from admin_operation.forms import UserImportForm,CampusInfoForm
from teacher_operation.forms import *
from admin_operation.models import UserImport
from django import forms
from user_management.models import *
from CourseAndScore.models import *
from django.http import HttpResponse,HttpResponseRedirect
import xlrd
from django.views.generic.edit import UpdateView
# Create your views here.

def t_scoreimport(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]
		uname = request.session["uname"]
		u_id = request.session["u_id"]
		data = []
		sign_t = False
		if request.method == 'POST':
			xf = UserImportForm(request.POST,request.FILES)
			#pdb.set_trace()
			#dir(xf)
			if xf.is_valid():
				userImport = xf.save()
				file = xlrd.open_workbook(userImport.xlsfile.path)
				# print( file.sheet_names() )
				sheet = file.sheet_by_index(0)
				# print( sheet.name,sheet.nrows,sheet.ncols )
				for n in range(sheet.nrows):
					data.append(sheet.row_values(n))
				data.pop(0)
				score_list = list()
				for i in data:
					stu = Student.objects.filter(name=i[0])
					cou = Course.objects.filter(name=i[1])
					score_list.append(Score(
						student=stu[0],
						course=cou[0],
						grade=str(int(i[2])),
						credit=str(int(i[3])),
					))
				# print(score_list)
				Score.objects.bulk_create(score_list)
				sign_t = True
		else:
			xf = UserImport()
		return render_to_response('score_upload.html',{'sign_t':sign_t,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
	else:
		return HttpResponseRedirect('/login/')

# Personal page for display and modification

# def personal(request):
# 	is_login = request.session.get('login',False)
# 	sex = 1
# 	grade =3
# 	department = 10
# 	s_list = ['男','女']
# 	g_list = ['大一','大二','大三','大四']
# 	d_list = ['中文系','政法系','外语系','数学系','物理系','化学系','生物系','音乐系','美术系','体育系','计算机系']
# 	if is_login:
# 		sign = request.session["sign"]
# 		username = request.session["account"]		
# 		uname = request.session["uname"]
# 		alert = False
# 		print(sign)
# 		if request.method == 'POST':
# 			person = PersonForm(request.POST)
# 			if person.is_valid():
# 				name = person.cleaned_data['name']
# 				gender = person.cleaned_data['gender']
# 				grade = person.cleaned_data['grade']
# 				the_class = person.cleaned_data['the_class']
# 				department = person.cleaned_data['department']
# 				phone = person.cleaned_data['phone']
# 				address = person.cleaned_data['address']
# 				if sign == 1:
# 					obj = Student.objects.filter(account=username)
# 					obj.update(name=name,gender=gender,grade=grade,the_class=the_class,department=department,phone=phone,address=address)
# 					alert = True
# 					return render_to_response('personal.html',{'account':username,'sign':sign,'uname':uname,'obj':obj,'alert':alert})
# 				else:
# 					obj = Student.objects.filter(account=username)
# 					obj.update(name=name,gender=gender,grade=grade,the_class=the_class,department=department,phone=phone,address=address)
# 					alert = True
# 					return render_to_response('personal.html',{'account':username,'sign':sign,'uname':uname,'obj':obj,'alert':alert})
# 		else:
# 			person = PersonForm()
# 			if sign == 1:
# 				obj = Student.objects.filter(account=username)[0]
# 			else:
# 				obj = Teahcer.objects.filter(account=username)[0]
# 			return render_to_response('personal.html',{'person':person,'account':username,'sign':sign,'uname':uname,'obj':obj,'sex':sex,'grade':grade,'department':department,'s_list':s_list,'g_list':g_list,'d_list':d_list})
# 	else:
# 		return HttpResponseRedirect('/login/')


class PersonUpdate(UpdateView):
	model = Student
	fields = ['gender','grade','phone_num','address']
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
		print('+++++++++++++++++++++++++++++++++')
		if is_login:
			return super().get(self, request, *args, **kwargs)
		else:
			return HttpResponseRedirect('/login/')


# sign = request.session["sign"]
# 			username = request.session["account"]
# 			uname = request.session["uname"]
# 			u_id = request.session["u_id"]
# 			x = super(UpdateView,self).get_object()
# 			y = super(UpdateView,self).get_form()
# 			print(y)
# 			print(type(x))
# 			print('++++++++++++++++++++++++++++++++++++++')
# 			return render_to_response('user_management/student_update.html', {'form':y,'account':username,'sign':sign,'u_id':u_id,'uname':uname})