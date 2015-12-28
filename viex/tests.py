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

	def test_homepage_can_save_POST_request(self):
		request=HttpRequest()
		request.method='POST'
		#The name attribute of the input field is used, eg <input name='stock_input'> 
		#This will pretend to POST to the stock_input within the <input> tag
		request.POST['stock_input'] = 'Search Stocks'

		#Get the response
		response=home_page(request)
		
		self.assertEqual(Stock.objects.count(),1)
		new_stock=Stock.objects.first()
		self.assertEqual(new_stock.text,'Search Stocks')


	def home_page_redirects_after_POST(self):
		request=HttpRequest()
		request.method='POST'
		request.POST['stock_input'] = 'Search Stocks'

		response=home_page(request)

		self.assertEqual(response.status_code,302)
		self.assertEqual(response['location'],'/')

	def test_homepage_only_saves_when_required(self):
		request=HttpRequest()
		home_page(request)
		self.assertEqual(Stock.objects.count(),0)

	def test_homepage_displays_stocks(self):
		Stock.objects.create(text='NOV 1')
		Stock.objects.create(text='SLCA 2')

		request=HttpRequest()
		response=home_page(request)

		self.assertIn('NOV 1', response.content.decode())
		self.assertIn('SLCA 2', response.content.decode())

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