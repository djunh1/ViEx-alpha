from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string


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
		#The name attribute of the input field is used
		request.POST['stock_input']='A new Stock to search'

		#Get the response
		response=home_page(request)

		self.assertIn('A new Stock to search', response.content.decode())
		
		expected_html=render_to_string('home.html',{'new_stock_text': 'A new Stock to search'})
		self.assertEqual(response.content.decode(), expected_html)



