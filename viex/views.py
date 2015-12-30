from django.shortcuts import render,redirect
from django.http import HttpResponse
from viex.models import Stock, StockData

# Create your views here.
def home_page(request):

	return render(request,'home.html')

def new_stock(request):
	#For each new request, creates a new stock data object
	#This will eventually be all the stock data for the VI f
	#                                                      class Stock foriegn key
	stockData_=StockData.objects.create()
	Stock.objects.create(text=request.POST['stock_input'], stockData=stockData_)
	return redirect('/stocks/%d/' %(stockData_.id,))

def add_stock(request,stock_id):
	stockData_=StockData.objects.get(id=stock_id)
	Stock.objects.create(text=request.POST['stock_input'], stockData=stockData_)
	return redirect('/stocks/%d/' %(stockData_.id,))

def view_stocks(request,stock_id):
	#Gets the stock table stuff
	stockData_=StockData.objects.get(id=stock_id)
	return render(request,'stock.html',{'stocks':stockData_})