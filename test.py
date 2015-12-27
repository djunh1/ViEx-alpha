from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Check to see if you can get into the website
        self.browser.get('http://localhost:8000')

        # Look at browswer title 

        self.assertIn('Value Investing Exchange',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Value Investing Exchange',header_text)

        #Enter an item into the text box
        inputbox=self.browser.find_element_by_id('id_stock_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a stock')

        #Type NOV into a text box
        inputbox.send_keys('NOV')

        #When entered, NOV should appear on the sceen
        inputbox.send_keys(keys.ENTER)

        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text=='1: NOV' for row in rows))

        self.fail('Finish the test!')  

        #Other comments

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
