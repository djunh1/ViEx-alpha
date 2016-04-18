import os
from decimal import *
from django.db import connections
import re

'''
TO DO:

1- Enterprise Value - mkt value of common +
 mkt value of preferred(optional) +
 mkt value of debt(have this) +
 minority interest(have this) -
 cash/investments DONE.
'''

def stat_cleaner(ticker):
	tickerTest = re.search(r'B$', ticker)
	if tickerTest is not None:
		tickerNew = float(re.sub("[^0123456789\.]", "", ticker))*1000.0
	else:
		tickerNew = float(re.sub("[^0123456789\.]", "", ticker))
	return tickerNew


class mySQLdb_query(object):
	'''
	This logic will control all the Database querries needed for the view.

	Parameters:

	ticker-  The stock symbol to be used for the query
	'''
	def __init__(self,ticker):
		'''
		These initializations are hashes to provide the correct terms to search for in MySQL.  For example
		EBIT corresponds to a statementrow_id of 17 which will provide the EBIT figure.
		'''
		self.ticker = ticker
		self.revenue = 1
		self.netEarnings = 25
		self.eps = 49
		self.CF_operations = 98
		self.CF_CapEx = 99
		self.shareOutstanding = 91
		self.EBIT = 17
		self.DA = 93
		self.LTdebt = 73
		self.cashAndEquiv = 50
		self.acctRecievables = 55
		self.acctInvendory = 56
		self.currentAssets = 59
		self.totalLiabilities = 80
		self.shEquity = 88

	def clean_nonetype(self,statementData):
		if statementData is None:
			statementData = Decimal(0)
			return statementData
		else:
			return statementData

	def get_netnet_value(self):
		'''
		TO DO-

		1- Get current share price and calculate a discount to net net working cap

		***Put this in the Done pile #jimKelley- Can't write to the tuple, and I need too!***
		'''
		cashAndEquiv=self.get_statement_data(self.cashAndEquiv)
		acctRecievables=self.get_statement_data(self.acctRecievables)
		acctInentory=self.get_statement_data(self.acctInvendory)
		totsLiabData=self.get_statement_data(self.totalLiabilities)
		soData=self.get_statement_data(self.shareOutstanding)

		#list(['test' if v is None else v for v in list(acctInentory)])

		#judgeaway

		netnetCap=[]
		for d,r,y,z,o in zip(cashAndEquiv, acctRecievables, acctInentory, totsLiabData, soData):

			cashEquiv=self.clean_nonetype(d[1])
			acctRecievables=self.clean_nonetype(r[1])
			acctInentory=self.clean_nonetype(y[1])
			totsLiabData=self.clean_nonetype(z[1])
			soData=self.clean_nonetype(o[1])


			netnetCap.append((cashEquiv+Decimal(.75)*acctRecievables-Decimal(.5)*acctInentory-totsLiabData)/soData)

		return netnetCap

	def get_EV(self, mktCap):
		debt = self.get_statement_data(self.LTdebt)
		cash = self.get_statement_data(self.cashAndEquiv)
		cd =  debt[0][1] - cash[0][1]
		EV = mktCap+float(cd)
		return EV

	def get_NCAV(self):
		curAssetData = self.get_statement_data(self.currentAssets)
		totsLiabData = self.get_statement_data(self.totalLiabilities)
		shoutstData = self.get_statement_data(self.shareOutstanding)

		ncav = []
		for x,y,z in zip(curAssetData,totsLiabData,shoutstData):
			ncav.append((x[1]-y[1])*(1/z[1]))

		return ncav


	def get_EBITDA(self):
		ebitData = self.get_statement_data(self.EBIT)
		daData = self.get_statement_data(self.DA)
		ebitda = []
		for x,y in zip(ebitData,daData):
			ebitda.append(x[1]+y[1])

		return ebitda

	def get_statement_data(self,statementId):
		c=connections['default'].cursor()
		column_str = " sd.date , sd.amount "
		stockData = []

		final_str="SELECT %s FROM VIEX_stock_data.statementData sd INNER JOIN VIEX_stock_data.symbol s ON sd.symbol_id = s.id WHERE s.ticker='%s' AND sd.statementrow_id=%f AND sd.type='annual' LIMIT 4;" % (column_str, self.ticker,statementId)
		c.execute(final_str)
		stockData=c.fetchall()

		return stockData

	def get_free_cash_flow(self):
		'''
		TO DO

		Formula= FCF/share (have this) / (price per share)

		1- GET price per share
		'''
		cfoData=self.get_statement_data(self.CF_operations)
		cfcapexData=self.get_statement_data(self.CF_CapEx)
		soData=self.get_statement_data(self.shareOutstanding)
		fcf=[]
		for x,y,z in zip(cfoData,cfcapexData,soData):
			fcf.append((x[1]+y[1])/z[1])

		return fcf










