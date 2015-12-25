from django.test import TestCase
from django.core.urlresolvers import resolve
from viex.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found=resolve('/')
		self.assertEqual(found.func,home_page)