from django.test import TestCase

from stockData.forms import StockForm, EMPTY_ITEM_ERROR


class StockFormTest(TestCase):

	def test_form_renders_stock_text_input(self):
		form=StockForm()

		self.assertIn('class="form-control input-lg" ', form.as_p())

	def test_form_validation_for_blank(self):
		form=StockForm(data={'text': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])