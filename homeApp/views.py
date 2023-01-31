from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.http import HttpResponse
from fpdf import FPDF as fp
import os
# Create your views here.
def home(request):
	if request.method=='POST':
		uploaded_file=request.FILES['files']
		
		file1=uploaded_file.read()
		print(file1)
		text = file1.decode('utf-8')
		paragraph = text.split("\n")
		txtPdf=fp()
		txtPdf.add_page()
		txtPdf.set_font("Arial",size=14)
		ct=1
		for para in paragraph:
			txtPdf.cell(200,10,txt=str(para),ln=ct,align="C")
			ct+=1
		output_file=txtPdf.output("/home/reshma/text_to_pdf_converter/homeApp/result.pdf")
		
		
		
		return HttpResponse(output_file)

		
		
    	

	return render(request,'homeApp/home.html')