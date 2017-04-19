from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

# class UserProfile(models.Model):
# 	USER_TEACHER = 0
# 	USER_STUDENT = 1
# 	USER_CHOICES = (
# 		(USER_TEACHER, '教师'),
# 		(USER_STUDENT, '学生'),
# 	)

# 	GENDER_MAN = 0
# 	GENDER_WOMAN = 1
# 	GENDER_CHOICES = (
# 		(GENDER_MAN, '男'),
# 		(GENDER_WOMAN, '女'),
# 	)

# 	user = models.OneToOneField(User)
# 	name = models.CharField(max_length=30,verbose_name='姓名')
# 	gender = models.IntegerField(choices=GENDER_CHOICES, default=None,verbose_name='姓别')
# 	grade = models.CharField(max_length=30,verbose_name='年级')
# 	the_class = models.CharField(max_length=30,verbose_name='班级')
# 	department = models.CharField(max_length=30,verbose_name='系别')
# 	phone_num = models.CharField(max_length=12,blank=True,verbose_name='联系电话')
# 	address = models.TextField(max_length=140, blank=True,verbose_name='住址')
# 	identity = models.IntegerField(choices=USER_CHOICES, default=None,verbose_name='身份')


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
		(DPT_1,'中文系'),
		(DPT_2,'政法系'),
		(DPT_3,'外语系'),
		(DPT_4,'数学系'),
		(DPT_5,'物理系'),
		(DPT_6,'化学系'),
		(DPT_7,'生物系'),
		(DPT_8,'音乐系'),
		(DPT_9,'美术系'),
		(DPT_10,'体育系'),
		(DPT_11,'计算机系'),
	)
	grade = models.IntegerField(choices=GRADE_CHOICES, default=None, blank=True,verbose_name='年级')
	the_class = models.CharField(max_length=30, blank=True,verbose_name='班级')
	department = models.IntegerField(choices=DPT_CHOICES, blank=True, default=None,verbose_name='系别')
	
	class Meta:
		verbose_name = '系别班级'
		verbose_name_plural = '系别班级'

	def __str__(self):
		return self.the_class

class Teacher(models.Model):
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
	grade = models.ManyToManyField(GradeInfo,related_name='gradeclass_t',verbose_name='年级班级')
	phone_num = models.CharField(max_length=12,blank=True,verbose_name='联系电话')
	address = models.TextField(max_length=140, blank=True,verbose_name='住址')

	class Meta:
		verbose_name = '教师'
		verbose_name_plural = '教师'

	def save(self,*args,**kwargs):
		self.password = make_password(self.password)
		super(Teacher,self).save(*args,**kwargs)

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

	def save(self,*args,**kwargs):
		self.password = make_password(self.password)
		super(Student,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

class CampusInfo(models.Model):
	title = models.CharField(max_length=30,verbose_name='标题')
	content = models.TextField(verbose_name='内容')
	timestamp = models.DateTimeField(verbose_name='发布时间')

	class Meta:
		verbose_name = '校园资讯'
		verbose_name_plural = '校园资讯'