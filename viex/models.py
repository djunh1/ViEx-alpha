from django.db import models

# Create your models here.

class StockData(models.Model):
	pass

class Stock(models.Model):
	text=models.TextField(default='')
	stockData=models.ForeignKey(StockData, default=None)