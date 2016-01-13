import os
from django.db import connections


class mySQLdb_query(object):
	'''
	This logic will control all the Database querries needed for the view.

	Parameters:

	ticker-  The stock symbol to be used for the query
	'''
	def __init__(self,ticker):
		self.ticker=ticker
		

	def get_income_statement(self):
		c=connections['default'].cursor()
		column_str=" sd.date , sd.amount "
		stockData=[]
		
		final_str="SELECT %s FROM VIEX_stock_data.statementData sd INNER JOIN VIEX_stock_data.symbol s ON sd.symbol_id = s.id INNER JOIN VIEX_stock_data.statementRow sr ON sd.statementRow_Id=sr.rowOrder WHERE s.ticker='%s' AND sr.rowOrder=49 AND sd.type='annual' LIMIT 4;" % (column_str, self.ticker)
		c.execute(final_str)
		stockData=c.fetchall()

		return stockData

