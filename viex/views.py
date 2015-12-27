from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	
	#post request comes from the input, with name attribute being stock_item
	return render(request,'home.html',{'new_stock_text': request.POST.get('stock_item',''),})