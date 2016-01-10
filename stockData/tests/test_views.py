from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from django.utils.html import escape

from stockData.forms import StockForm, EMPTY_ITEM_ERROR
from stockData.models import Stock,StockData
from stockData.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	maxDiff=None

	def test_home_page_returns_right_html(self):
		response=self.client.get('/')
		self.assertTemplateUsed(response,'home.html')

	def test_home_page_uses_stock_form(self):
		response=self.client.get('/')
		self.assertIsInstance(response.context['form'], StockForm)

class stockInputTesting(TestCase):

	def post_invalid_input(self):
		pass


	def test_redirects_after_POST(self):
		pass

	def test_validation_errors_are_on_stocks_page(self):
		pass

	def test_invalid_input_renders_home_template(self):
		'''
		#Keep this
		response=self.post_invalid_input()
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'stock.html')
		'''

	def test_for_invalid_input_passes_form_to_template(self):
		pass

class StockDataViewTest(TestCase):



	def test_displays_stock_data(self):
		pass

	def test_displays_stock_form(self):
		'''
		stockData_=StockData.objects.create()
		response=self.client.get('/stocks/%d/' % (stockData_.id,))
		self.assertIsInstance(response.context['form'], StockForm)
		self.assertContains(response, 'name="text"')
		'''








