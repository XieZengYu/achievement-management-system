from django.contrib import admin
from CourseAndScore.models import *
from user_management.models import *
from user_management.admin import *
# Register your models here.
#foreignkey
class CourseInline(admin.TabularInline):
  	model = Course
  	extra = 1

class ScoreInline(admin.TabularInline):
  	model = Score
  	extra = 1

class GradesInline(admin.TabularInline):
	model = Course.grade_class.through
	extra = 1


class CourseAdmin(admin.ModelAdmin):
	list_display = ('name','credit','teacher')

	inlines = [
		ScoreInline,
		GradesInline,
	]

	
# Re-register UserAdmin
admin.site.register(Course,CourseAdmin)
admin.site.register(Score)
