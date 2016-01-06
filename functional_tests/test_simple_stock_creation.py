from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from .base import FunctionalTest


class NewVisitorTest(FunctionalTest): 
    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Check to see if you can get into the website
        self.browser.get(self.server_url)
        # Look at browswer title 

        self.assertIn('Value Investing Exchange',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Search for a stock',header_text)

        #Enter an item into the text box
        inputbox=self.browser.find_element_by_id('id_stock_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Search stocks...')

        #Type NOV into a text box
        inputbox.send_keys('NOV')

        #When entered, NOV should appear on the sceen
        inputbox.send_keys(Keys.ENTER)
        stock_url=self.browser.current_url
        #Make the url as follows
        self.assertRegex(stock_url,'/stocks/.+')
        self.check_row_in_table('1: NOV')


        #Type SLCA into a text box
        inputbox=self.browser.find_element_by_id('id_stock_item')
        inputbox.send_keys('SLCA')
        #When entered, SLCA should appear on the sceen
        inputbox.send_keys(Keys.ENTER)

        self.check_row_in_table('2: SLCA')
        self.check_row_in_table('1: NOV')

        
        #New User should arrive to home page and see nothing

        self.browser.get(self.server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('NOV',page_text)
        self.assertNotIn('SLCA',page_text)

        #At this point, the user ends their session
        self.browser.quit()
        self.browser=webdriver.Firefox()

        #Fire up a new session
        self.browser.get(self.server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('NOV', page_text)
        self.assertNotIn('SLCA', page_text)

        #New User starts new stock list

        inputbox=self.browser.find_element_by_id('id_stock_item')
        inputbox.send_keys('AAPL')
        inputbox.send_keys(Keys.ENTER)

        #New User gets thier own URL
        newUser_list_url=self.browser.current_url
        self.assertRegex(newUser_list_url,'/stocks/.+')
        self.assertNotEqual(newUser_list_url,stock_url)

        #Checking there is no previous list here

        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('NOV',page_text)
        self.assertIn('AAPL',page_text)


        #self.fail('Good to go')  

        #Other comments


