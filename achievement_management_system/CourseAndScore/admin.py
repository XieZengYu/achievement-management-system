from django.contrib import admin
from CourseAndScore.models import *
# Register your models here.

# Re-register UserAdmin
admin.site.register(Course)
admin.site.register(Score)
