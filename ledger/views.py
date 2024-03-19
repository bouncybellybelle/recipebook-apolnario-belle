from django.contrib.auth.decorators import *
from django.shortcuts import *
from django.views.generic import *
from django.views.generic.list import *
from django.views.generic.detail import *
from django.contrib.auth.mixins import *

from .models import *


class RecipesListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailsView(LoginRequiredMixin, TemplateView):
    model = Recipe
    template_name = 'ledger/recipes.html'
    redirect_field_name = 'ledger/login.html'  # url to redirect when not logged in
