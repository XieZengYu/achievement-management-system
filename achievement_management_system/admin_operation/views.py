from django.shortcuts import render,render_to_response
from admin_operation.forms import UserImportForm,CampusInfoForm
from admin_operation.models import UserImport
from user_management.models import *
from CourseAndScore.models import *
from django.http import HttpResponse,HttpResponseRedirect
import xlrd
# Create your views here.

def userimport(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]		
		uname = request.session["uname"]
		u_id = request.session['u_id']
		data = []
		sign1 = False
		if request.method == 'POST':
			xf = UserImportForm(request.POST,request.FILES)
			check_sign = request.POST.getlist("inlineRadioOptions")
			# import pdb; pdb.set_trace()
			#dir(check_sign)
			if xf.is_valid():
				userImport = xf.save()
				file = xlrd.open_workbook(userImport.xlsfile.path)
				print( file.sheet_names() )
				sheet = file.sheet_by_index(0)
				print( sheet.name,sheet.nrows,sheet.ncols )
				for n in range(sheet.nrows):
					data.append(sheet.row_values(n))
				data.pop(0)
				#judege the student or teacher ,if the value is 1,student
				if check_sign[0] == '1':
					student_list = list()
					for i in data:
						grinfo, _ = GradeInfo.objects.get_or_create(
							grade= str(int(i[4])),
							the_class= i[5],
							department= str(int(i[6])),
						)
						student_list.append(Student(
							account=str(int(i[0])),
							password=str(int(i[1])),
							name=i[2],
							gender=str(int(i[3])),
							grade =grinfo,
							phone_num=str(int(i[7])),
							address=i[8],
						))
						# import pdb; pdb.set_trace()
					print(student_list)
					Student.objects.bulk_create(student_list)
				else:
					teacher_list = list()
					for i in data:
						grinfo, _ = GradeInfo.objects.get_or_create(
							grade= str(int(i[4])),
							the_class= i[5],
							department= str(int(i[6])),
						)
						teacher = Teacher(
							account=str(int(i[0])),
							password=str(int(i[1])),
							name=i[2],
							gender=str(int(i[3])),
							phone_num=str(int(i[7])),
							address=i[8],
						)
						teacher.save()
						teacher.grade.add(grinfo)
						teacher_list.append(teacher)
					print(teacher_list)
					sign1 =True
		else:
			xf = UserImport()
		return render_to_response('user_upload.html',{'sign1':sign1,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
	else:
		return HttpResponseRedirect('/login/')

def courseimport(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]		
		uname = request.session["uname"]
		u_id = request.session['u_id']
		data = []
		sign2 = False
		if request.method == 'POST':
			xf = UserImportForm(request.POST,request.FILES)
			#pdb.set_trace()
			#dir(xf)
			if xf.is_valid():
				userImport = xf.save()
				file = xlrd.open_workbook(userImport.xlsfile.path)
				print( file.sheet_names() )
				sheet = file.sheet_by_index(0)
				print( sheet.name,sheet.nrows,sheet.ncols )
				for n in range(sheet.nrows):
					data.append(sheet.row_values(n))
				data.pop(0)
				course_list = list()
				for i in data:
					grinfo, _ = GradeInfo.objects.get_or_create(
							grade= str(int(i[4])),
							the_class= i[5],
							department= str(int(i[6])),
						)
					course = Course(
						name=i[0],
						number=str(int(i[1])),
						intro=i[2],
						credit=str(int(i[3])),
					)
					course.save()
					course.grade_class.add(grinfo)
					course_list.append(course)
				print(course_list)
				sign2 = True
		else:
			xf = UserImport()
		return render_to_response('course_upload.html',{'sign2':sign2,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
	else:
		return HttpResponseRedirect('/login/')

def scoreimport(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]		
		uname = request.session["uname"]
		u_id = request.session['u_id']
		data = []
		sign3 = False
		if request.method == 'POST':
			xf = UserImportForm(request.POST,request.FILES)
			#pdb.set_trace()
			#dir(xf)
			if xf.is_valid():
				userImport = xf.save()
				file = xlrd.open_workbook(userImport.xlsfile.path)
				print( file.sheet_names() )
				sheet = file.sheet_by_index(0)
				print( sheet.name,sheet.nrows,sheet.ncols )
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
				print(score_list)
				Score.objects.bulk_create(score_list)
				sign3 = True
		else:
			xf = UserImport()
		return render_to_response('score_upload.html',{'sign3':sign3,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
	else:
		return HttpResponseRedirect('/login/')


def campusinfo(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]		
		uname = request.session["uname"]
		u_id = request.session['u_id']
		if request.method == 'POST':
			info = CampusInfoForm(request.POST)
			if info.is_valid():
				title = info.cleaned_data['title']
				content = info.cleaned_data['content']
				CampusInfo.objects.create(title=title,content=content)
				return HttpResponseRedirect('/index/')
		else:
			info = CampusInfoForm()
		return render_to_response('upnews.html',{'info':info,'account':username,'sign':sign,'uname':uname,'u_id':u_id})
	else:
		return HttpResponseRedirect('/login/')