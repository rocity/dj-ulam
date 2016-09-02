from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Recipe

# Create your views here.
def home_page(request):

    recipes = Recipe.objects.all()

    if request.method == 'POST':
        new_recipe_title = request.POST['title_text']
        new_recipe_ingredient = request.POST['ingredient_text']
        Recipe.objects.create(
            title=new_recipe_title,
            ingredient=new_recipe_ingredient
            )
        return redirect('/')


    return render(request, 'create.html', {'recipes': recipes})
