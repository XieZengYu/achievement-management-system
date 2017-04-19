from django.shortcuts import render,render_to_response
from admin_operation.forms import UserImportForm
from admin_operation.models import UserImport
from user_management.models import *
from CourseAndScore.models import *
from django.http import HttpResponse
import xlrd
# Create your views here.

def userimport(request):
	data = []
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
	else:
		xf = UserImport()
	return render_to_response('user_upload.html',{'data':data})

def courseimport(request):
	data = []
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
	else:
		xf = UserImport()
	return render_to_response('course_upload.html',{'data':data})

def scoreimport(request):
	data = []
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
	else:
		xf = UserImport()
	return render_to_response('score_upload.html',{'data':data})
