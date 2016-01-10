from django import forms

from stockData.models import Stock

EMPTY_ITEM_ERROR="Please search for a valid stock symbol..."

class StockForm(forms.models.ModelForm):

	class Meta:
		model=Stock
		fields=('text',)
		widgets= {
		'text': forms.fields.TextInput(attrs={
			'placeholder': 'Search for a stock...',
			'class': 'form-control input-lg'
			}),
		}
		error_messages={'text' : { 'required': EMPTY_ITEM_ERROR}
		}

	def save(self,for_stock):
		self.instance.stock=for_stock
		return super().save()