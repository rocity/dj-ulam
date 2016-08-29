from selenium import webdriver
import unittest
import time

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

        # He is invited to create a recipe straight away
        titlebox = self.browser.find_element_by_id('id_recipe_title')
        self.assertEqual(
            titlebox.get_attribute('placeholder'),
            'What is your dish called?'
            )

        # He types on the title, "Apple Pie"
        titlebox.send_keys('Apple Pie')

        # He notices a field for the ingredients
        recipebox = self.browser.find_element_by_id('id_recipe_ingre')
        self.assertEqual(
            recipebox.get_attribute('placeholder'),
            'An ingredient for your dish?'
            )

        # He types an ingredient
        recipebox.send_keys('Lemon Juice')

        # When he clicks the Submit button, the page updates, and now the page
        # displays "Apple Pie" as a dish, and "Lemon Juice" as its recipe
        submitbutton = self.browser.find_element_by_id('id_submit_recipe')
        submitbutton.click()

        time.sleep(10)

        table = self.browser.find_element_by_id('id_recipe_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Apple Pie', [row.text for row in rows])
        self.assertIn('Lemon Juice', [row.text for row in rows])

        # There is still a text box inviting him to add another ingredient.
        # He enters "Sliced Apples"
        self.fail('Finish the test!')

        # Clyde wonders if the site will remember his recipe. Then he sees
        # that the site has generated a unique URL for him

        # He visits the URL and his recipe is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
