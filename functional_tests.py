from selenium import webdriver
import unittest

class NewVisitorTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_recipe_and_retrieve_it_later(self):
        # Clyde has heard about a cool new online app where you can get random dishes
        # to try and cook. He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title mention Ulam
        self.assertIn('Ulam', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to create a recipe straight away

        # He types on the title, "Adobo"

        # He types on 3 ingredients

        # Clyde wonders if the site will remember his recipe. Then he sees
        # that the site has generated a unique URL for him

        # He visits the URL and his recipe is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
