from django.shortcuts import render,redirect

from viex.models import Stock, StockData
from django.core.exceptions import ValidationError

# Create your views here.
def home_page(request):
	return render(request,'home.html')

def new_stock(request):
	#For each new request, creates a new stock data object
	#This will eventually be all the stock data for the VI f
	#                                                      class Stock foriegn key
	stockData_=StockData.objects.create() #Create the list for the stocks
	stock=Stock(text=request.POST['stock_input'], stockData=stockData_) #Create the stock , foriegn key is 'stockData'
	try:
		stock.full_clean()
		stock.save()
	except ValidationError:
		stockData_.delete()
		error="Please search for a valid stock symbol..."
		return render(request, 'home.html', {"error": error})
	return redirect(stockData_)

def view_stocks(request,stock_id):
	#Gets the stock table stuff
	stockData_=StockData.objects.get(id=stock_id)
	error=None

	if request.method=='POST':
		try:
			
			stock=Stock(text=request.POST['stock_input'], stockData=stockData_)
			stock.full_clean()
			stock.save()
			return redirect(stockData_)
		except ValidationError:
			error="Please search for a valid stock symbol..."
	return render(request,'stock.html',{'stocks':stockData_, 'error':error})