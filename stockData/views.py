from django.shortcuts import render

from stockData.forms import StockForm
from django.core.exceptions import ValidationError

from django.db import connections

# Create your views here.
def home_page(request):
	c=connections['default'].cursor()
	c.execute('SELECT * FROM VIEX_stock_data.symbol')
	tickers=c.fetchall()
	print(tickers[2687][2])
	return render(request,'home.html', {'form': StockForm(), 'stocks':tickers[2][2]})


def view_stock_info(request):
	pass