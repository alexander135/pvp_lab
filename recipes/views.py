from django.contrib.auth import authenticate, logout, login as auth_login
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from recipes.forms import LoginForm, CommentForm
from recipes.models import Recipe, Comment, Like
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import simplejson
from django.contrib.contenttypes.models import ContentType


def recipe_detail(request, recipe_id):
    recipes = Recipe.objects.select_related().get(pk = recipe_id)
    return render (
            request, 'recipes/recipe_detail.html',
            {'recipes': recipes}
            )


def author_detail(request, author_id):
    recipes = Recipe.objects.filter(author_id=author_id)
    return render(
        request, 'recipes/author_detail.html',
        {'recipes': recipes}
    )



def all_recipes(request):
    rec = Recipe.objects.all()
    p = Paginator(rec, 5)
    page = request.GET.get('page')
    recipes = p.get_page(page)
    return render(
            request, 'recipes/all_recipes.html',
            {'recipes': recipes}
            )


def all_authors(request):
    recipes = Recipe.objects.all()
    return render(
            request, 'recipes/all_authors.html',
            {'recipes':recipes}
            )




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/recipes/')
                else:
                    return HttpResponse('<h1>user is not active</h1>')
            else:
                return HttpResponse('<h1>user does not exist</h1>')
        else:
            return render (
                    request, 'recipes/login.html',
                    {'form':form}
                    )
    else:
        form = LoginForm()
        return render(
            request, 'recipes/login.html',
            {'form': form}
            )

def home_page(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'anonymous'
    return render(
            request, 'recipes/home_page.html',
            {'username':  username}
            )

def content_recipe(request, page_number):
    rec = Recipe.objects.all()
    p = Paginator(rec, 5)
    page = page_number
    recipes = p.get_page(page)
    return render(request, 'recipes/content_recipe.html',
             {'recipes': recipes})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/recipes/')


from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "../login/"

    template_name = "recipes/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


class RecipeFormView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title','preview','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def commentForm(request, recipe_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            recipe = Recipe.objects.get(id = recipe_id)
            comment = Comment(content_object = recipe)
            comment.comment_text = form.cleaned_data['comment_text']
            comment.creator = request.user
            comment.save()
            return HttpResponse(simplejson.dumps({'response': "ok", 'result': 'success'}))
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
                return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
    else:
        form = CommentForm()
        recipe = Recipe.objects.get(id=recipe_id)
        comment = recipe.comments.last()
        return render(request, 'recipes/comment.html', {'form': form, 'comment': comment})

def like(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    recipe_type = ContentType.objects.get_for_model(recipe)
    if Like.objects.filter(content_type__pk=recipe_type.id, object_id=recipe_id, liker=request.user).exists():
        Like.objects.filter(content_type__pk=recipe_type.id, object_id=recipe_id, liker=request.user).delete()
    else:
        Like.objects.create(liker=request.user, content_object=recipe)
    count = recipe.likes.count()
    return HttpResponse(count)
"""
def get_recipe(request):
    since = request.Get.get("since",0)
    recipe = Recipe.objects.filter(created_at__gt = since)
    return HttpResponse(recipe.title)

"""

''' 
def Registration(request):
    if requset.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == forms.cleaned_data['password_confirm']: 
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = UserModel.objects.create_user(username = username, password = password)
                auth_login(request, user)
                return HttpResponseRedirect('/recipes/')
            else
                return     
        '''