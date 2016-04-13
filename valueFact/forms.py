from django import forms

from valueFact.models import Comment, Stock


EMPTY_ITEM_ERROR="Please search for a valid stock symbol..."

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

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
		error_messages={'text': { 'required': EMPTY_ITEM_ERROR }
		}

	def save(self, for_stock):
		self.instance.stock=for_stock
		return super().save()