from django.db import models

# Create your models here.
class UserImport(models.Model):
	#name = models.CharField(max_length = 50)
	xlsfile = models.FileField(upload_to = './material/upload/')
