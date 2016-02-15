from django.test import 
import unittest

from django.core.exceptions import ValidationError
from stockData.models import Stock




class StockDataAndStockModelTest(TestCase):
	
	@unittest.skip
	def test_get_absolute_url(self):
		Stock_=Stock.objects.create()
		self.assertEqual(response.get_absolute_url(),'/stocks/SDRL')
