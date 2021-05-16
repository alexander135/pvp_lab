from django.contrib.auth import get_user_model
from recipes.models import Recipe, Comment, Like, Ingredient, Complaint

UserModel = get_user_model()
insert_list = []
user = UserModel.objects.get(pk = 1)
for k in range(10000):
     i = k+20025
     title = "String number %s" %i
     text = "text %s" %i
     preview  = "preview %s" %i
     insert_list.append(Recipe(title=title, text = text, preview = preview, author = user))
Recipe.objects.bulk_create(insert_list)