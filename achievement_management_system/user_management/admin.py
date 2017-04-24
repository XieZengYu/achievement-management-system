from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user_management.models import *

#ForeignKey
class StudentInline(admin.TabularInline):
  	model = Student

#ManyToMany
class GradeInline(admin.TabularInline):
	model = Teacher.grade.through

class StudentAdmin(admin.ModelAdmin):
	list_display = ('account','name','gender','grade_grade','grade_department','grade_the_class','phone_num')
	
	def grade_grade(self,obj):
			return obj.grade.grade
	def grade_department(self,obj):
			return obj.grade.department
	def grade_the_class(self,obj):
			return obj.grade.the_class

	#raw_id_fields =("grade",)

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('account','name','gender','phone_num')
	inlines = [
		GradeInline,
	]
	raw_id_fields =("grade",)

class GradeInfoAdmin(admin.ModelAdmin):
	inlines = [
		StudentInline,
		GradeInline,
	]


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(GradeInfo,GradeInfoAdmin)
admin.site.register(CampusInfo)