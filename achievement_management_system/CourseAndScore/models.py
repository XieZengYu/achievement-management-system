from django.db import models
from user_management.models import *
# Create your models here.
class Course(models.Model):
	CREDIT_1 = 1
	CREDIT_2 = 2
	CREDIT_3 = 3
	CREDIT_CHOICES =(
		(CREDIT_1,'1'),
		(CREDIT_2,'2'),
		(CREDIT_3,'3'),
	)

	name = models.CharField(max_length=30,verbose_name='课程名称')
	number = models.CharField(max_length=10,verbose_name='课程编号')
	intro = models.CharField(max_length=140,verbose_name='课程简介')
	credit = models.IntegerField(choices=CREDIT_CHOICES, default=None,verbose_name='学分')
	teacher = models.ManyToManyField(Teacher,related_name='course_t',verbose_name='授课教师')
	student = models.ManyToManyField(Student,related_name='course_s',verbose_name='学生')

class Score(models.Model):
	student = models.ForeignKey(Student,verbose_name='学生')
	course = models.ForeignKey(Course,verbose_name='课程名称')
	grade = models.CharField(max_length=5,verbose_name='成绩')
	credit = models.IntegerField(verbose_name='所获学分')