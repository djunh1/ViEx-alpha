from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip
import unittest
import sys


#class NewVisitorTest(LiveServerTestCase):  
class FunctionalTest(StaticLiveServerTestCase):
    
    @classmethod    
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url='http://'+arg.split('=')[1]
                return #
        super().setUpClass()
        cls.server_url=cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url==cls.live_server_url:
            super().tearDownClass()

    def setUp(self):  
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()

    def get_stock_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

