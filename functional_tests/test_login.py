from selenium.webdriver.support.ui import WebDriverWait
from .base import FunctionalTest

import time

TEST_EMAIL = 'dj@mockmyid.com'

class LoginTest(FunctionalTest):

	def switch_to_new_window(self,text_in_title):
		retries =10
		while retries >0:
			for handle in self.browser.window_handles:
				self.browser.switch_to_window(handle)
				if text_in_title in self.browser.title:
					return
			retries -=1
			time.sleep(0.5)
		self.fail('Could not find window')

	def test_login_with_persona(self):
		#User wants to log in to the value investing exchange
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_login').click()

		#Login window appears
		self.switch_to_new_window('Mozilla Persona')

		#Log in with an email address
		self.browser.find_element_by_id('authentication_email').send_keys(TEST_EMAIL)
		self.browser.find_element_by_tag_name('button').click()

		#Switch to new window
		self.switch_to_new_window('Value Investing Exchange')

		#Check that you are logged in
		self.wait_to_be_logged_in(email=TEST_EMAIL)

		#refresh page to check for a session login.

		self.browser.refresh()
		self.wait_to_be_logged_in(email=TEST_EMAIL)

		#User sees that they are loged into the switch_to_new_window
		self.browser.find_element_by_id('id_logout').click()
		self.wait_to_be_logged_out(email=TEST_EMAIL)

		#Loged out status will exist during a refresh

		self.browser.refresh()
		self.wait_to_be_logged_out(email=TEST_EMAIL)



