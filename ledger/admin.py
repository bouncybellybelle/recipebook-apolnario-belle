from django.contrib import admin

from .models import *


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
