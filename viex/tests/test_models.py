from django.test import TestCase

from django.core.exceptions import ValidationError
from viex.models import Stock,StockData




class StockDataAndStockModelTest(TestCase):
	
	def test_saving_retrieving_stocks(self):
		#Creates and saves an instance of the stock data object
		stockData_=StockData()
		stockData_.save()

		first_stock=Stock()
		first_stock.text='First stock on list'
		first_stock.stockData=stockData_
		first_stock.save()

		second_stock=Stock()
		second_stock.text='Second stock on list'
		second_stock.stockData=stockData_
		second_stock.save()

		saved_stockData=StockData.objects.first()
		self.assertEqual(saved_stockData,stockData_)

		saved_stocks=Stock.objects.all()
		self.assertEqual(saved_stocks.count(),2)

		first_saved_stock=saved_stocks[0]
		second_saved_stock=saved_stocks[1]
		self.assertEqual(first_saved_stock.text,'First stock on list')
		self.assertEqual(first_saved_stock.stockData, stockData_)
		self.assertEqual(second_saved_stock.text,'Second stock on list')
		self.assertEqual(second_saved_stock.stockData, stockData_)

	def test_can_not_search_empty_stocks(self):
		stockData=StockData.objects.create()
		stock=Stock(stockData=stockData, text='')
		with self.assertRaises(ValidationError):
			stock.save()
			stock.full_clean()

	def test_get_absolute_url(self):
		stockData_=StockData.objects.create()
		self.assertEqual(stockData_.get_absolute_url(), '/stocks/%d/' %(stockData_.id,))
