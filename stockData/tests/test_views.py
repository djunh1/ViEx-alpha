from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from django.utils.html import escape

from stockData.forms import StockForm, EMPTY_ITEM_ERROR
from stockData.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	maxDiff=None

	def test_home_page_renders_Homepage(self):
		response=self.client.get('/')
		self.assertTemplateUsed(response,'home.html')


	def test_home_page_uses_stock_form(self):
		response=self.client.get('/')
		#Checks to see if this view uses the right form.
		self.assertIsInstance(response.context['form'], StockForm)




class newStockSearchTest(TestCase):

	def post_invalid_input(self):
		pass


	def test_redirects_after_POST(self):
		pass


	def test_validation_errors_are_on_stocks_page(self):
		response=self.client.post('/stocks/', data={'text':''})
		expected_error=escape(EMPTY_ITEM_ERROR)
		self.assertContains(response,expected_error)


	def test_invalid_input_renders_home_template(self):
		response=self.client.post('/stocks/', data={'text':''})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'stockData.html')


	def test_for_invalid_input_passes_form_to_template(self):
		response=self.client.post('/stocks/', data={'text':''})
		self.assertIsInstance(response.context['form'],StockForm)

	def test_is_correct_ticker_being_used(self):
		#Check that the ticker searched is correct.  Use SDRL as a test
		response=self.client.post('/stocks/', data={'text':'SDRL'})
		sdrlData=response.context['ticker']
		self.assertEqual(sdrlData,'SDRL')

	def test_stock_data_freeCashFlow_fetching(self):
		#Will the data be correct?  Search for NOV
		#In 2014 the free cash flow was 4.57 million dollars
		response=self.client.post('/stocks/', data={'text':'NOV'})
		novData=format(response.context['fcf'][0], '.2f')
		self.assertEqual(novData,'4.57')

	def test_stock_data_eps_fetching(self):
		#Check EPS data of Apple , AAPL
		#EPS in 2015 was 5.09 dollars per share
		response=self.client.post('/stocks/', data={'text':'AAPL'})
		aaplData=format(response.context['eps'][1][1], '.2f')
		self.assertEqual(aaplData,'5.09')

	def test_stock_data_ncav_fetching(self):
		#Check Net current asset value of data of
		#NCAV for Waters in 2015 was 
		response=self.client.post('/stocks/', data={'text':'WAT'})
		aaplData=format(response.context['ncav'][1][1], '.2f')
		self.assertEqual(aaplData,'10.47')

	def test_stock_data_netnet_fetching(self):
		#Check net net working capital data of TGA
		#net net working capital of 
		response=self.client.post('/stocks/', data={'text':'SDRL'})
		aaplData=format(response.context['netnet'][1][1], '.2f')
		self.assertEqual(aaplData,'5.09')

	def test_data_has_none(self):
		'''
		Anything with 'none' in the data.  has to be handled correctly
		'''
		response=self.client.post('/stocks/', data={'text':'ASAX'})













