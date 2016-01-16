
from .base import FunctionalTest


class StockValidationTest(FunctionalTest):

    def test_can_not_add_empty_stockTicker(self):
    	pass

    def test_error_messages_cleared_on_unput(self):
    	self.browser.get(self.server_url)
    	self.get_stock_input_box().send_keys('\n')

    	error=self.get_error_element()
    	self.assertTrue(error.is_displayed())

    	self.get_stock_input_box().send_keys('PSX')

    	error=self.get_error_element()
    	self.assertFalse(error.is_displayed())

        
