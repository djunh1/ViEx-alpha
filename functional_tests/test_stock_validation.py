from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip

from .base import FunctionalTest

class StockValidationTest(FunctionalTest):

    def test_can_not_add_empty_stockTicker(self):

        #User attempts to submit a blank stock
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_stock_item').send_keys('\n')

        #Home page to refresh with error message
        error=self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Please enter a stock to search")

        #Input a ticker.  Should work
        self.browser.find_element_by_id('id_stock_item').send_keys('WAT')
        self.check_row_in_table('1: WAT')

        #Put in another blank item.  Warning appears
        self.browser.find_element_by_id('id_stock_item').send_keys('\n')

        self.check_row_in_table('1: WAT')
        error=self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "Please enter a stock to search")
        
        #Eliminate error by inputting text
        self.browser.find_element_by_id('id_stock_item').send_keys('GTAT')
        self.check_row_in_table('1: WAT')
        self.check_row_in_table('2: GTAT')

        self.fail('End of test')
