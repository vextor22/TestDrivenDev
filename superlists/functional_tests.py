from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

#looks at page title
class NewVisitorTest(unittest.TestCase):

		
		def setUp(self):
				self.browser = webdriver.Firefox()
				self.browser.implicitly_wait(3)

		def tearDown(self):
				self.browser.quit()

		def check_for_row_in_list_table(self, row_text):
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])

		def test_can_start_a_list_and_retrieve_it_later(self):
				self.browser.get('http://127.0.0.1:8000')

				self.assertIn('To-Do', self.browser.title)

				header_text = self.browser.find_element_by_tag_name('h1').text
				self.assertIn('To-Do', header_text)
				#user is prompted for item
				inputbox = self.browser.find_element_by_id('id_new_item')
				self.assertEqual(
								inputbox.get_attribute('placeholder'),
								'Enter a to-do item'
								)

				#add an item to the list
				inputbox.send_keys('Buy peacock feathers')
				inputbox.send_keys(Keys.ENTER)
				time.sleep(2)
				inputbox = self.browser.find_element_by_id('id_new_item')

				inputbox.send_keys('Use peacock feathers to make a fly')
				inputbox.send_keys(Keys.ENTER)
				time.sleep(1)
				#page is updated with the item
				self.check_for_row_in_list_table('1: Buy peacock feathers')
				self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

				self.fail('Finish the test!')

				#add another item to the list
				#navigate to unique url to verify list persists
if __name__ == '__main__':
		unittest.main(warnings='ignore')
