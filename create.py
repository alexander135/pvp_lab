from django.contrib.auth import get_user_model
from recipes.models import Recipe, Comment, Like, Ingredient, Complaint
from django.utils import timezone
from datetime import datetime, date, time

UserModel = get_user_model()

for i in range(100):
    k = str(i)

    

    recipe = Recipe(title = 'title'+k ,text = 'text' + k, preview ='preview' + k)
    recipe.author = UserModel.objects.get(pk = 1)
    recipe.save()

    ingredient = Ingredient (ingredient_name = 'ingredient' + k)
    ingredient.dish = Recipe.objects.get(pk = i+1)
    ingredient.save()

    comment = Comment(creator=)

