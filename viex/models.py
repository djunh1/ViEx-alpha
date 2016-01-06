from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class StockData(models.Model):
	
	def get_absolute_url(self):
		return reverse('view_stocks', args=[self.id])

class Stock(models.Model):
	text=models.TextField(default='')
	stockData=models.ForeignKey(StockData, default=None)