from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user_management.models import *

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(GradeInfo)
admin.site.register(CampusInfo)