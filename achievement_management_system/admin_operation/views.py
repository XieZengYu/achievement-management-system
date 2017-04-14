from django.shortcuts import render,render_to_response
from admin_operation.forms import UserImportForm
from admin_operation.models import UserImport
from django.http import HttpResponse
import xlrd
import pdb
# Create your views here.

def userimport(request):
	data = []
	if request.method == 'POST':
		xf = UserImportForm(request.POST,request.FILES)
		#pdb.set_trace()
		#dir(xf)
		if xf.is_valid():
			xf.save()
			file = xlrd.open_workbook(xf.fields['xlsfile'].filename)
			print( file.sheet_names() )
			sheet = file.sheet_by_index(0)
			print( sheet.name,sheet.nrows,sheet.ncols )
			for n in range(sheet.nrows):
				data.append(sheet.row_values(n))
		
	else:
		xf = UserImport()
	return render_to_response('upload_test.html',{'data':data})
