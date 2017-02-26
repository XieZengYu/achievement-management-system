from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	USER_TEACHER = 0
	USER_STUDENT = 1
	USER_CHOICES = (
		(USER_TEACHER, '教师'),
		(USER_STUDENT, '学生'),
	)

	GENDER_MAN = 0
	GENDER_WOMAN = 1
	GENDER_CHOICES = (
		(GENDER_MAN, '男'),
		(GENDER_WOMAN, '女'),
	)

	user = models.OneToOneField(User)
	name = models.CharField(max_length=30)
	gender = models.IntegerField(choices=GENDER_CHOICES, default=None)
	phone_num = models.IntegerField(max_length=11, blank=True)
	address = models.TextField(max_length=140, blank=True)
	identity = models.IntegerField(choices=USER_CHOICES, default=None)