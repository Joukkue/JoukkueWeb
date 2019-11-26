from django.shortcuts import render, redirect
import sqlite3
from sys import platform
from django.contrib.auth import authenticate, login, logout
from django import forms
from JoukkuePage import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import HttpResponseRedirect
from collections import OrderedDict

from WebCode.models import Quote, Levels, TelegramChat


class LoginForm(forms.Form):

    username = forms.CharField(label='', widget=forms.TextInput(attrs = {'class': 'form-control' , 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'password'}))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required to activate account.')
    #override default -> required = True
    first_name = forms.CharField(max_length=30, help_text = 'Required to greet you in a friendly way', required = True)


def getContext():
    context = {'loginform': LoginForm}
    return context


def frontpage(request):
    context = getContext()
    return render(request, "home.html", context)


@login_required
def show(request):
    quotes = Quote.objects.all()
    context = getContext()
    context['quotes'] = quotes
    return render(request, "quotes.html", context)


def login_user(request):
    loginform = LoginForm()
    context = {'user': request.user, 'loginform': loginform}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(settings.LOGIN_SUCCESS_URL)
        else:
            return redirect(settings.LOGIN_FAIL_URL)
    else:
        # should this do something?
        pass


def login_page(request):
    return render(request, "loginpage.html", getContext())


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/loginpage/')


def signup(request):
    loginform = LoginForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if settings.EMAIL_CONFIRMATION_REQUIRED:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
            return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'loginform': loginform})


def get_levels(request):
    levels = Levels.objects.all().order_by('-level').order_by('-exp')
    chats = TelegramChat.objects.all()
    dictionary = {}
    for chat in chats:
        dictionary[chat.chatName] = []
    for level in levels:
        dictionary[level.chatid.chatName].append(level)
    context = {'stuff': dictionary}
    return render(request, "levels.html", context)
