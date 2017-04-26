from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class GradeInfo(models.Model):
	GRADE_1 = 1
	GRADE_2 = 2
	GRADE_3 = 3
	GRADE_4 = 4
	GRADE_CHOICES = (
		(GRADE_1,'大一'),
		(GRADE_2,'大二'),
		(GRADE_3,'大三'),
		(GRADE_4,'大四'),
	)

	DPT_1 = 1
	DPT_2 = 2
	DPT_3 = 3
	DPT_4 = 4
	DPT_5 = 5
	DPT_6 = 6
	DPT_7 = 7
	DPT_8 = 8
	DPT_9 = 9
	DPT_10 = 10
	DPT_11 = 11
	DPT_CHOICES = (
		(DPT_1,u'中文系'),
		(DPT_2,u'政法系'),
		(DPT_3,u'外语系'),
		(DPT_4,u'数学系'),
		(DPT_5,u'物理系'),
		(DPT_6,u'化学系'),
		(DPT_7,u'生物系'),
		(DPT_8,u'音乐系'),
		(DPT_9,u'美术系'),
		(DPT_10,u'体育系'),
		(DPT_11,u'计算机系'),
	)
	grade = models.IntegerField(choices=GRADE_CHOICES, default=None, blank=True,verbose_name='年级')
	the_class = models.CharField(max_length=30, blank=True,verbose_name='班级')
	department = models.IntegerField(choices=DPT_CHOICES, blank=True, default=None,verbose_name='系别')
	
	class Meta:
		verbose_name = '系别班级'
		verbose_name_plural = '系别班级'

	def __str__(self):
		return "%s%s%s"%(dict(GradeInfo.DPT_CHOICES)[self.department],dict(GradeInfo.GRADE_CHOICES)[self.grade],self.the_class)

class Teacher(models.Model):
	GENDER_MAN = 0
	GENDER_WOMAN = 1
	GENDER_CHOICES = (
		(GENDER_MAN, '男'),
		(GENDER_WOMAN, '女'),
	)

	DPT_1 = 1
	DPT_2 = 2
	DPT_3 = 3
	DPT_4 = 4
	DPT_5 = 5
	DPT_6 = 6
	DPT_7 = 7
	DPT_8 = 8
	DPT_9 = 9
	DPT_10 = 10
	DPT_11 = 11
	DPT_CHOICES = (
		(DPT_1,u'中文系'),
		(DPT_2,u'政法系'),
		(DPT_3,u'外语系'),
		(DPT_4,u'数学系'),
		(DPT_5,u'物理系'),
		(DPT_6,u'化学系'),
		(DPT_7,u'生物系'),
		(DPT_8,u'音乐系'),
		(DPT_9,u'美术系'),
		(DPT_10,u'体育系'),
		(DPT_11,u'计算机系'),
	)

	account = models.CharField(max_length=15,unique = True,verbose_name='帐号')
	password = models.CharField(max_length=15,verbose_name='密码')
	name = models.CharField(max_length=30,verbose_name='姓名')
	gender = models.IntegerField(choices=GENDER_CHOICES, default=None,verbose_name='姓别')
	department = models.IntegerField(choices=DPT_CHOICES,verbose_name='系别')
	phone_num = models.CharField(max_length=12,blank=True,verbose_name='联系电话')
	address = models.TextField(max_length=340, blank=True,verbose_name='住址')

	class Meta:
		verbose_name = '教师'
		verbose_name_plural = '教师'

	# def save(self,*args,**kwargs):
	# 	self.password = make_password(self.password)
	# 	super(Teacher,self).save(*args,**kwargs)

	def __str__(self):
		return self.name


class Student(models.Model):
	GENDER_MAN = 0
	GENDER_WOMAN = 1
	GENDER_CHOICES = (
		(GENDER_MAN, '男'),
		(GENDER_WOMAN, '女'),
	)

	account = models.CharField(max_length=15,unique = True,verbose_name='帐号')
	password = models.CharField(max_length=15,verbose_name='密码')
	name = models.CharField(max_length=30,verbose_name='姓名')
	gender = models.IntegerField(choices=GENDER_CHOICES, default=None,verbose_name='姓别')
	grade = models.ForeignKey(GradeInfo,verbose_name='年级班级')
	phone_num = models.CharField(max_length=12,blank=True,verbose_name='联系电话')
	address = models.TextField(max_length=140, blank=True,verbose_name='住址')

	class Meta:
		verbose_name = '学生'
		verbose_name_plural = '学生'

	# def save(self,*args,**kwargs):
	# 	self.password = make_password(self.password)
	# 	super(Student,self).save(*args,**kwargs)

	def __str__(self):
		return "%s%s"%(self.grade.the_class,self.name)

class CampusInfo(models.Model):
	title = models.CharField(max_length=30,verbose_name='标题')
	content = models.TextField(verbose_name='内容')
	timestamp = models.DateTimeField(auto_now=True,verbose_name='发布时间')

	class Meta:
		ordering = ['-timestamp']
		verbose_name = '校园资讯'
		verbose_name_plural = '校园资讯'

	def __str__(self):
		return self.title