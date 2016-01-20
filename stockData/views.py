from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db import connections

from stockData.forms import StockForm
from stockData.controller import mySQLdb_query

'''
Using custom controller with own MYSQL queries.  Don't hate.

TO DO-

1- WRite a test for no data.  DONE 
2- Write the template for a stock not being found
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

			print(stockQueryDb.get_statement_data(stockQueryDb.eps))
			if stockQueryDb.get_statement_data(stockQueryDb.eps)==():
				return render(request,'home.html',{'form':StockForm()})
			else:
				#Returns EPS data
				epsData=stockQueryDb.get_statement_data(stockQueryDb.eps)
				fcfData=stockQueryDb.get_free_cash_flow()
				stockQueryDb.get_netnet_value()
				ncavData=stockQueryDb.get_NCAV()[1]
				netnetData=stockQueryDb.get_netnet_value()[1]
			
				return render(request,'stockData.html',{'eps': epsData , 'fcf': fcfData, 'ncav': ncavData, 'netnet':netnetData,"form":form , "ticker":ticker})
	
	return render(request,'home.html',{ "form":form })
