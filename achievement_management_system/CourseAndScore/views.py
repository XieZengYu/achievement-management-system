from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django import forms
from user_management.models import *
from CourseAndScore.models import *
# Create your views here.
def course(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]
		uname = request.session["uname"]
		u_id = request.session['u_id']
		if sign == 1:
			course = Student.objects.filter(account=username).first().grade.course_class.all()		
		else:	
			course = []
			c = Course.objects.filter(teacher__account=username).all()
			for x in c:
				a = ''
				for q in x.grade_class.all():
					a +=( dict(GradeInfo.GRADE_CHOICES)[q.grade] + dict(GradeInfo.DPT_CHOICES)[q.department] + q.the_class + ' ' )
				course.append([x.name,x.number,a,x.credit])
		return render_to_response('course.html', {'course':course,'account':username,'sign':sign,'u_id':u_id,'uname':uname})
	else:
		return HttpResponseRedirect('/login/')

def score(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]
		uname = request.session["uname"]
		u_id = request.session['u_id']
		score = []
		if sign == 1:
			c = Score.objects.filter(student__account=username)
			for x in c:
				score.append([x.course.name,x.grade,x.course.credit,x.credit])
			print(score)
		else:
			#find the course
			d = Course.objects.filter(teacher__account=username)
			for c in d:
				#find the class
				S = []
				for x in c.grade_class.all():
					a = ''
					a += ( dict(GradeInfo.GRADE_CHOICES)[x.grade] + dict(GradeInfo.DPT_CHOICES)[x.department] + x.the_class + ' ' )
					#find the score
					t = Score.objects.filter(course__teacher__account=username,course=c)
					L = []
					for i in t:
						L.append([i.course.name, a, i.student.name, i.grade, i.credit])
					S.append(L)
				score.append(S)
		return render_to_response('score.html', {'score':score,'account':username,'sign':sign,'u_id':u_id,'uname':uname})
	else:
		return HttpResponseRedirect('/login/')

def analyze(request):
	is_login = request.session.get('login',False)
	if is_login:
		sign = request.session["sign"]
		username = request.session["account"]
		uname = request.session["uname"]
		u_id = request.session['u_id']
		analyze = []
		if sign == 1:
			c = Score.objects.filter(student__account=username)
			for x in c:
				tc = Score.objects.filter(course__name=x.course.name).order_by('-grade')
				for i,obj in enumerate(tc):
					if obj.student.account == username:
						index = i + 1
				analyze.append({'1':x.course.name,'2':x.grade,'3':index})
			print(analyze)
		else:
			#find the course
			d = Course.objects.filter(teacher__account=username)
			for c in d:
				#find the class
				S = []
				for x in c.grade_class.all():
					a = ''
					a += ( dict(GradeInfo.GRADE_CHOICES)[x.grade] + dict(GradeInfo.DPT_CHOICES)[x.department] + x.the_class + ' ' )
					#find the score
					t = Score.objects.filter(course__teacher__account=username,course=c).order_by('-grade')
					L = []
					for i,obj in enumerate(t):
						index = i + 1
						L.append({'1':obj.course.name,'2':a,'3':obj.student.name,'4':obj.grade,'5':index})
					S.append(L)
				analyze.append(S)
				print(analyze)
		return render_to_response('analyze.html', {'analyze':analyze,'account':username,'sign':sign,'u_id':u_id,'uname':uname})
	else:
		return HttpResponseRedirect('/login/')