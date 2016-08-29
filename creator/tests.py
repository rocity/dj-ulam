from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from creator.views import home_page

TITLE_TEXT = 'A new recipe'

# Create your tests here.
class HomePageTestCase(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('create.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['title_text'] = TITLE_TEXT

        response = home_page(request)
        self.assertIn(TITLE_TEXT, response.content.decode())

        expected_html = render_to_string(
            'create.html',
            {'title_text': TITLE_TEXT}
            )
        self.assertEqual(response.content.decode(), expected_html)
