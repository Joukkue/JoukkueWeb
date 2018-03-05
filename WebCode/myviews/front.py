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
    if platform == "linux":
        connection = sqlite3.connect('/home/pi/JoukkueBot/joukkue.db')
    else:
        connection = sqlite3.connect('joukkue.db')
        #connection = sqlite3.connect('/home/pi/JoukkueBot/joukkue.db')
    c = connection.cursor()
    c.execute('SELECT * FROM Quotes')
    quotes = c.fetchall()
    context = getContext()
    context['quotes'] = {}
    for quote in quotes:
        asd = {quote[1]:quote[2]}
        context['quotes'][quote[0]] = asd
    print (quotes)
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
    if platform == "linux":
        connection = sqlite3.connect('/home/pi/JoukkueBot/joukkue.db')
    else:
        connection = sqlite3.connect('joukkue.db')
    c = connection.cursor()
    context = OrderedDict()
    my_dict = OrderedDict()
    c.execute("SELECT * FROM Chats ORDER BY name")
    chats = c.fetchall()
    for chat in chats:
        my_dict[chat[0]] = OrderedDict()
        t = chat[1]
        c.execute("SELECT * FROM Levels WHERE chat =? ORDER BY level DESC, experience DESC ", (t,))
        levels = c.fetchall()
        for level in levels:
            exp_and_level = {level[2]:level[3]}
            username_and_level = {level[0]:exp_and_level}
            chat_and_username = {chat[0]:username_and_level}
            my_dict[chat[0]][level[0]] = exp_and_level
            context = {'my_dict': my_dict}
    #print (levels)
    print(context)



    return render(request, "levels.html", context)
