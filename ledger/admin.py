# from django.contrib import admin
#
# from .models import *
#
#
# class RecipeIngredientAdmin(admin.TabularInline):
#     model = RecipeIngredient
#
#
# class RecipeAdmin(admin.ModelAdmin):
#     model = Recipe
#     inlines = [RecipeIngredientAdmin, ]
#
#
# class IngredientAdmin(admin.ModelAdmin):
#     model = Ingredient
#
#
# admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Ingredient, IngredientAdmin)


from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import admin

from .models import *


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.BaseUserAdmin):
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, BaseUserAdmin)
