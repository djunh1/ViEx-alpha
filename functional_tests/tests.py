from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time


class NewVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()

    def check_row_in_table(self,row_text):
        table=self.browser.find_element_by_id('id_stock_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Check to see if you can get into the website
        self.browser.get(self.live_server_url)

        # Look at browswer title 

        self.assertIn('Value Investing Exchange',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Search for a Stock Symbol',header_text)

        #Enter an item into the text box
        inputbox=self.browser.find_element_by_id('id_stock_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Search stocks...')

        #Type NOV into a text box
        inputbox.send_keys('NOV')

        #When entered, NOV should appear on the sceen
        inputbox.send_keys(Keys.ENTER)
        stock_url=self.browser.current_url
        self.assertRegex(stock_url,'/stocks/.+/')
        self.check_row_in_table('1: NOV')

        #Type SLCA into a text box
        inputbox=self.browser.find_element_by_id('id_stock_item')
        inputbox.send_keys('SLCA')
        time.sleep(5)
        #When entered, SLCA should appear on the sceen
        inputbox.send_keys(Keys.ENTER)

        self.check_row_in_table('2: SLCA')
        self.check_row_in_table('1: NOV')

        #At this point, the user ends their session
        self.browser.quit()
        self.browser=webdriver.Firefox()

        #New User should arrive to home page and see nothing

        self.browser.get(self.live_server_url)
        page_test=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('1: NOV',page_text)
        self.assertNotIn('2: SLCA',page_text)

        #New User starts new stock list

        inputbox=self.browser.find_element_by_id('id_stock_item')
        inputbox.send_keys('AAPL')
        inputbox.send_keys(Keys.ENTER)


        self.fail('All tests up to this point passed.  Keep testing...')  

        #Other comments


