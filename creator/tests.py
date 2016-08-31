from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from creator.views import home_page

from creator.models import Recipe

TITLE_TEXT = 'A new recipe'
INGREDIENT_TEXT = 'one ingredient'

# Create your tests here.

class ItemModelTestCase(TestCase):
    def test_saving_and_retrieving_recipes(self):
        first_recipe = Recipe()
        first_recipe.title = 'Banana Pop'
        first_recipe.ingredient = 'Ice'
        first_recipe.save()

        saved_recipes = Recipe.objects.all()
        self.assertEqual(saved_recipes.count(), 1)

        first_saved_recipe = saved_recipes[0]
        self.assertEqual(first_saved_recipe.title, 'Banana Pop')
        self.assertEqual(first_saved_recipe.ingredient, 'Ice')

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
        request.POST['ingredient_text'] = INGREDIENT_TEXT

        response = home_page(request)

        self.assertEqual(Recipe.objects.count(), 1)
        new_recipe = Recipe.objects.first()
        self.assertEqual(new_recipe.title, TITLE_TEXT)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Recipe.objects.count(), 0)
