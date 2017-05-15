from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user_management.models import *
from CourseAndScore.models import *
from CourseAndScore.admin import *
#ForeignKey
# class StudentInline(admin.TabularInline):
#   	model = Student
#   	extra = 1

class ScoreInline(admin.TabularInline):
  	model = Score
  	extra = 1

class StudentAdmin(admin.ModelAdmin):
	list_display = ('account','name','gender','grade','phone_num')
	inlines = [
		ScoreInline,
	]

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('account','name','gender','department','phone_num')
	inlines = [
		CourseInline,
	]

class GradeInfoAdmin(admin.ModelAdmin):
	inlines = [
		# StudentInline,
		GradesInline,
	]


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(GradeInfo,GradeInfoAdmin)
admin.site.register(CampusInfo)