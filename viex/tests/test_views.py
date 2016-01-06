from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from django.utils.html import escape

from viex.models import Stock,StockData
from viex.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found=resolve('/')
		self.assertEqual(found.func, home_page)

	def test_homepage_returns_correct_html(self):
		request=HttpRequest()

		response=home_page(request)

		expected_html=render_to_string('home.html')
		self.assertEqual(response.content.decode(),expected_html)

class newStocklistTest(TestCase):

	def test_save_stock_on_existing_list_POST(self):

		self.client.post('/stocks/new' ,data={'stock_input': 'Search Stocks..'})

		self.assertEqual(Stock.objects.count(),1)
		new_stock=Stock.objects.first()
		self.assertEqual(new_stock.text,'Search Stocks..')


	def test_redirects_after_POST(self):

		response=self.client.post('/stocks/new', data={'stock_input': 'Search Stocks..'})
		
		new_stocks=StockData.objects.first()
		self.assertRedirects(response, '/stocks/%d/' % (new_stocks.id,))

	def test_validation_errors_are_on_stocks_page(self):

		response=self.client.post('/stocks/new' ,data={'stock_input': ''})
		
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response, 'home.html')
		expected_error=escape("Please search for a valid stock symbol...")
		self.assertContains(response,expected_error)	


	def test_invalid_input_doesnt_save(self):
		self.client.post('/stocks/new', data={'stock_input': ''})
		self.assertEqual(StockData.objects.count(),0)
		self.assertEqual(Stock.objects.count(),0)


class StockDataViewTest(TestCase):

	def test_displays_stocks(self):
		
		correct_stockData=StockData.objects.create()
		Stock.objects.create(text='NOV 1' ,stockData=correct_stockData)
		Stock.objects.create(text='SLCA 2',stockData=correct_stockData)
		
		other_stockData=StockData.objects.create()
		Stock.objects.create(text='MSFT 1' ,stockData=other_stockData)
		Stock.objects.create(text='AAPL 2',stockData=other_stockData)
		#client.get fetches the url to test
		response=self.client.get('/stocks/%d/' %(correct_stockData.id,))

		#AssertContains knows how to deal with responses and the bytes of their content
		self.assertContains(response,'NOV 1')
		self.assertContains(response,'SLCA 2')
		self.assertNotContains(response, 'MSFT 1')
		self.assertNotContains(response, 'AAPL 2')
		

	def test_uses_stock_template(self):
		stockData_=StockData.objects.create()
		response=self.client.get('/stocks/%d/' % (stockData_.id,))
		self.assertTemplateUsed(response,'stock.html')








