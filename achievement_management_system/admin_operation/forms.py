from django.forms import ModelForm
from admin_operation.models import UserImport
# Create your models here.
class UserImportForm(ModelForm):
	class Meta:
		model = UserImport
		fields = '__all__'
