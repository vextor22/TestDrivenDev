from selenium import webdriver
import unittest


#looks at page title
class NewVisitorTest(unittest.TestCase):

		
		def setUp(self):
				self.browser = webdriver.Firefox()
				self.browser.implicitly_wait(3)

		def tearDown(self):
				self.browser.quit()

		def test_can_start_a_list_and_retrieve_it_later(self):
				self.browser.get('http://127.0.0.1:8000')

				self.assertIn('To-Do', self.browser.title)
				self.fail('Finish the test!')

#add an item to the list
#add another item to the list
#navigate to unique url to verify list persists
if __name__ == '__main__':
		unittest.main(warnings='ignore')
