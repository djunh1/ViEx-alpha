from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db import connections

from stockData.forms import StockForm
from stockData.controller import mySQLdb_query

'''
Using custom controller with own MYSQL queries.  Don't hate.
'''
def home_page(request):
	return render(request,'home.html', {'form': StockForm()})

def stock_data_search_display(request):
	form=StockForm()
	
	if request.method=='POST':
		form=StockForm(data=request.POST)
		stockData=[]
		if form.is_valid():
			ticker=form.cleaned_data['text']
			stockQueryDb=mySQLdb_query(ticker)
			stockData=stockQueryDb.get_income_statement()
			
			return render(request,'stockData.html',{'eps': stockData , "form":form , "ticker":ticker})
	
	return render(request,'stockData.html',{ "form":form })
