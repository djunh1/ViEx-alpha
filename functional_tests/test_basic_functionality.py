from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from .base import FunctionalTest


class AdminTest(FunctionalTest):

    def test_admin_site(self):
        self.browser.get(self.server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)


class StaticPageTest(FunctionalTest):

    def test_basic_search_url(self):
        self.browser.get(self.server_url + '/companies/')
        # Look for a search box
        inputBox = self.browser.find_element_by_id('id_text')
        self.assertIn('Search for a stock...', inputBox.get_attribute('placeholder'))


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


        self.fail('Continue writing tests')  




