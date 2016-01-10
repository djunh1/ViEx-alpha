from django.test import TestCase

from django.core.exceptions import ValidationError
from stockData.models import Stock




class StockDataAndStockModelTest(TestCase):
	
	'''
	def test_can_not_search_empty_stocks(self):
		stockData=StockData.objects.create()
		stock=Stock(stockData=stockData, text='')
		with self.assertRaises(ValidationError):
			stock.save()
			stock.full_clean()

	'''
