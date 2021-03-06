from django import forms

from valueFact.models import Comment, Stock


DEFAULT_ERRORS= {
	'required': 'This field is required',
	'invalid': 'Please enter a valid value'
}

EMPTY_ITEM_ERROR = "Please search for a valid stock symbol..."


class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')


class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(required=True, widget=forms.Textarea)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['content'].label = "Enter a message here"


class StockForm(forms.models.ModelForm):

	class Meta:
		model = Stock
		fields = ('text',)
		widgets = {
		'text': forms.fields.TextInput(attrs={
			'placeholder': 'Search for a stock...',
			'class': 'form-control input-lg'
		}),
		}

		error_messages = {'text': {'required': EMPTY_ITEM_ERROR}}

	def save(self, for_stock):
		self.instance.stock = for_stock
		return super().save()