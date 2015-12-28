from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):  

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
        self.browser.get('http://localhost:8000')

        # Look at browswer title 

        self.assertIn('Value Investing Exchange',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Search for a Stock Symbol',header_text)

        #Enter an item into the text box
        inputbox=self.browser.find_element_by_id('id_stock_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a Stock')

        #Type NOV into a text box
        inputbox.send_keys('NOV')

        #When entered, NOV should appear on the sceen
        inputbox.send_keys(Keys.ENTER)

        time.sleep(.1)
        table=self.browser.find_element_by_id('id_stock_table')
        rows=table.find_elements_by_tag_name('tr')
        
        
        self.check_row_in_table('1: NOV')
        self.check_row_in_table('2: SLCA')

        self.fail('Finish the test!')  

        #Other comments

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
