from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_recipe_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_recipe_and_retrieve_it_later(self):
        # Clyde has heard about a cool new online app where you can get random dishes
        # to try and cook. He goes to check out its homepage
        self.browser.get(self.live_server_url)

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

        # When he hits enter, he is taken to a new URL,
        # and now the page lists: Apple Pie, Lemon Juice as an item in a
        # recipe table
        submitbutton = self.browser.find_element_by_id('id_submit_recipe')
        submitbutton.click()

        time.sleep(10)
        clyde_recipe_url = self.browser.current_url
        self.assertRegex(clyde_recipe_url, '/recipes/.+')

        # The page updates again, and now shows both items on his recipe
        self.check_for_row_in_table('Apple Pie')
        self.check_for_row_in_table('Lemon Juice')

        # Now a new user, Clynt, comes along to the site.

        ## We use a new browser session to make sure that no info
        ## of Clyde's is coming through from cookies etc#
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Clynt visits the home page. There is no sign of Clyde's recipe
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_elements_by_tag_name('body').text
        self.assertNotIn('Apple Pie', page_text)
        self.assertNotIn('Lemon', page_text)

        # Clynt starts a new recipe by entering a new item. He is
        # less interesting than Clyde...
        inputbox = self.browser.find_element_by_id('id_recipe_title');
        inputbox.send_keys('Clementine Cake')

        submitbutton = self.browser.find_element_by_id('id_submit_recipe')
        submitbutton.click()

        # Clynt gets his own unique URL
        clynt_recipe_url = self.browser.current_url
        self.assertRegex(clynt_recipe_url, '/recipes/.+')
        self.assertNotEqual(clynt_recipe_url, clyde_recipe_url)

        # Again, there is no trace of Clyde's list
        page_text = self.browser.find_elements_by_tag_name('body').text
        self.assertNotIn('Apple Pie', page_text)
        self.assertIn('Clementine Cake', page_text)

        # Satisfied, he goes back to sleep
        self.fail('Finish the test!')
