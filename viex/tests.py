from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from viex.models import Stock
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

class NewStockTest(TestCase):

	def test_can_save_POST_request(self):

		'''
		Use this to check posts are saved during a POST request.
		request=HttpRequest()
		request.method='POST'
		#The name attribute of the input field is used, eg <input name='stock_input'> 
		#This will pretend to POST to the stock_input within the <input> tag
		request.POST['stock_input'] = 'Search Stocks'

		#Get the response
		response=home_page(request)
		Refactored to below:
		'''

		#No trailing slash in url means action url, these modify the db
		self.client.post('/stocks/new', data={'stock_input': 'Search Stocks..'})
		
		self.assertEqual(Stock.objects.count(),1)
		new_stock=Stock.objects.first()
		self.assertEqual(new_stock.text,'Search Stocks..')
	
	def test_redirects_after_POST(self):
		'''
		use this to check that the page is redirected after a stock is searched
		'''
	
		response=self.client.post('/stocks/new', data={'stock_input': 'Search Stocks..'})
		
		#This checks to see if the url redirects to the required URL
		self.assertRedirects(response, '/stocks/one_persons_stock_list/')


class StockModelTest(TestCase):
	
	def test_saving_retrieving_stocks(self):
		first_stock=Stock()
		first_stock.text='First stock on list'
		first_stock.save()

		second_stock=Stock()
		second_stock.text='Second stock on list'
		second_stock.save()

		saved_stocks=Stock.objects.all()
		self.assertEqual(saved_stocks.count(),2)

		first_saved_stock=saved_stocks[0]
		second_saved_stock=saved_stocks[1]
		self.assertEqual(first_saved_stock.text,'First stock on list')
		self.assertEqual(second_saved_stock.text,'Second stock on list')

class LiveViewTest(TestCase):

	def test_displays_stocks(self):
		Stock.objects.create(text='NOV 1')
		Stock.objects.create(text='SLCA 2')

		#client.get fetches the url to test
		response=self.client.get('/stocks/one_persons_stock_list/')

		#AssertContains knows how to deal with responses and the bytes of their content
		self.assertContains(response,'NOV 1')
		self.assertContains(response,'SLCA 2')

	def test_uses_stock_template(self):
		response=self.client.get('/stocks/one_persons_stock_list/')
		self.assertTemplateUsed(response,'stock.html')

