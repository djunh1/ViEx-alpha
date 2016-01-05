from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip

from .base import FunctionalTest

class StockValidationTest(FunctionalTest):

    def test_can_not_add_empty_stockTicker(self):

        #User attempts to submit a blank stock

        #Home page to refresh with error message

        #Input a ticker.  Should work

        #Put in another blank item.  Warning appears

        #Eliminate error by inputting text

        self.fail('End of test')
