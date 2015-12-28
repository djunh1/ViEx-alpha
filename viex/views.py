from django.shortcuts import render
from django.http import HttpResponse
from viex.models import Stock

# Create your views here.
def home_page(request):
	
	if request.method=='POST':
		new_stock_text=request.POST['stock_input']
		Stock.objects.create(text=new_stock_text)
	else:
		new_stock_text=''

	return render(request,'home.html',{'new_stock_text': new_stock_text,})