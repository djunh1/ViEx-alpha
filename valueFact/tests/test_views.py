from django.test import SimpleTestCase, TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from django.utils.html import escape

from valueFact.forms import StockForm, EMPTY_ITEM_ERROR
from valueFact.views import home_page


class HomePageTest(TestCase):
	def test_home_page_renders_homepage(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main_page/home.html')

	def test_home_page_renders_faq(self):
		response = self.client.get('/faq/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'faq/faq.html')

	def test_home_page_renders_toc(self):
		response = self.client.get('/toc/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'toc/toc.html')

	def test_home_page_uses_stock_form(self):
		pass





class newStockSearchTest(SimpleTestCase):

	def post_invalid_input(self):
		pass


	def test_redirects_after_POST(self):
		pass












