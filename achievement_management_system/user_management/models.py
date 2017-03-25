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

class Teacher(models.Model):
	GENDER_MAN = 0
	GENDER_WOMAN = 1
	GENDER_CHOICES = (
		(GENDER_MAN, '男'),
		(GENDER_WOMAN, '女'),
	)

	account = models.CharField(max_length=15,verbose_name='帐号')
	password = models.CharField(max_length=15,verbose_name='密码')
	name = models.CharField(max_length=30,verbose_name='姓名')
	gender = models.IntegerField(choices=GENDER_CHOICES, default=None,verbose_name='姓别')
	grade = models.CharField(max_length=30,verbose_name='年级')
	the_class = models.CharField(max_length=30,verbose_name='班级')
	department = models.CharField(max_length=30,verbose_name='系别')
	phone_num = models.CharField(max_length=12,blank=True,verbose_name='联系电话')
	address = models.TextField(max_length=140, blank=True,verbose_name='住址')
	def save(self,*args,**kwargs):
		self.password = make_password(self.password)
		super(Teacher,self).save(*args,**kwargs)


class Student(models.Model):
	GENDER_MAN = 0
	GENDER_WOMAN = 1
	GENDER_CHOICES = (
		(GENDER_MAN, '男'),
		(GENDER_WOMAN, '女'),
	)

	account = models.CharField(max_length=15,verbose_name='帐号')
	password = models.CharField(max_length=15,verbose_name='密码')
	name = models.CharField(max_length=30,verbose_name='姓名')
	gender = models.IntegerField(choices=GENDER_CHOICES, default=None,verbose_name='姓别')
	grade = models.CharField(max_length=30,verbose_name='年级')
	the_class = models.CharField(max_length=30,verbose_name='班级')
	department = models.CharField(max_length=30,verbose_name='系别')
	phone_num = models.CharField(max_length=12,blank=True,verbose_name='联系电话')
	address = models.TextField(max_length=140, blank=True,verbose_name='住址')
	def save(self,*args,**kwargs):
			self.password = make_password(self.password)
			super(Student,self).save(*args,**kwargs)