from django.shortcuts import *
from django.views.generic.list import *
from django.views.generic.detail import *

from .models import *


class RecipesListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'ledger/recipes.html'
