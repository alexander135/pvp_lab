from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username', max_length = 50)
    password = forms.CharField(label = 'password', widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label = 'имя пользовател',max_length = 50)
    password = forms.CharField(label = 'пароль' , widget = forms.PasswordInput )
    passwoed_confirm = forms.CharField(label='повторите пароль', widget = forms.PasswordInput)


class CommentForm(forms.Form):
    comment_text = forms.CharField(label = 'ваш комментарий', max_length=200)

