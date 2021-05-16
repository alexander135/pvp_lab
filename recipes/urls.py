from django.conf.urls import url
from django.urls import path
from recipes.views import *

urlpatterns = [
        path('all_recipes/<int:recipe_id>/', recipe_detail, name = 'recipe_detail'),
        path('author/<int:author_id>/', author_detail, name = 'author_detail'),
        path('all_recipes/', all_recipes, name = 'all_recipes'),
        path('all_authors/', all_authors, name = 'all_authors'),
        path('login/', login, name = 'login'),
        path('logout/', logout_view, name = 'logout'),
        path('', home_page, name = 'home_page'),
        path('register/', RegisterFormView.as_view()),
        path('content_recipe/<int:page_number>/', content_recipe, name = 'content_recipe'),
        path('create_recipe/', RecipeFormView.as_view()),
        path('commentForm/<int:recipe_id>/', commentForm, name = 'commentForm'),
        path('like/<int:recipe_id>/', like, name = "like"),
#        path("get_recipe", get_recipe, name = "get_recipe"),
        ]
