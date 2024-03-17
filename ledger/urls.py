from django.urls import path

from .views import *

urlpatterns = [
    path('list/', RecipesListView.as_view(), name='recipes_list'),
    path('<int:pk>/detail', CustomView.as_view(), name='recipe_detail'), ]

app_name = "ledger"
