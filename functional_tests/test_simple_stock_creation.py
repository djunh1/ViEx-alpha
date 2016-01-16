from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from .base import FunctionalTest


class NewVisitorTest(FunctionalTest): 

    def test_can_search_stocks_and_get_information(self):  
        '''
        This will check basic functionality of inputting and searching for stock information from
        the MySQL DB. 

        TO DO -

        Eventually expand this test to include the "facts" once they are designed.  For now, stick
        to just the raw SQL data. 
        '''
        # Check to see if you can get into the website
        self.browser.get(self.server_url)

        # Check that browser title is correct ( this shows that the right page is loaded)
        self.assertIn('Value Investing Exchange',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Search for a stock',header_text)

        #Enter a stock into a text box -  In this case, lets check out Seadrill ticker SDRL

        inputbox=self.get_stock_input_box()

        inputbox.send_keys('SDRL')


        #Here is what needs to come up.  Check the URL, and rows in the table

        #Type another stock into the text box

        #Check what comes up.  Check URL etc

        #Close browser.  User should see normal home page where they can enter a stock

        #New user should see their unique stock selection and their own data.  Make sure previous 
        #Input is gone as well


        self.fail('Continue writing tests')  

        #Other comments


