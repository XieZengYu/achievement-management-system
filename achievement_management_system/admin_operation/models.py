from django.db import models

# Create your models here.
class UserImport(models.Model):
	xlsfile = models.FileField()
