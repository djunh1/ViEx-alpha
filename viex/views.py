from django.shortcuts import render,redirect
from django.http import HttpResponse
from viex.models import Stock

# Create your views here.
def home_page(request):
	
	if request.method=='POST':

		Stock.objects.create(text=request.POST['stock_input'])
		return redirect('/')
	stocks=Stock.objects.all()

	return render(request,'home.html',{'stocks':stocks})