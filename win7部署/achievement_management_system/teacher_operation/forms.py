from django.forms import ModelForm
from django import forms
from admin_operation.models import *
from user_management.models import *
# Create your models here.
class PersonForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

