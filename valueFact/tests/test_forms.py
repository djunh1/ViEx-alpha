from django.test import SimpleTestCase

from valueFact.forms import StockForm, EMPTY_ITEM_ERROR


class StockFormTest(SimpleTestCase):

	def test_form_renders_stock_text_input(self):
		pass
		'''
		form = StockForm()
		self.assertIn('class="form-control input-lg" ', form.as_p())
		'''

	def test_form_validation_for_blank(self):
		pass
		'''
		form=StockForm(data={'text': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])
		'''

	def test_form_has_placeholder_and_css(self):
		pass
		'''
		form=StockForm()
		self.assertIn('placeholder="Search for a stock..."', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())
		'''