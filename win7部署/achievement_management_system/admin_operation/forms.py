from django.forms import ModelForm
from django import forms
from admin_operation.models import UserImport
from user_management.models import CampusInfo
# Create your models here.
class UserImportForm(ModelForm):
	class Meta:
		model = UserImport
		fields = '__all__'


class CampusInfoForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)
