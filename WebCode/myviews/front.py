from django.shortcuts import render
import sqlite3
from sys import platform

def frontpage(request):
    return render(request, "home.html")

def show(request):
    if platform == "linux":
        connection = sqlite3.connect('/home/pi/JoukkueBot/joukkue.db')
    else:
        connection = sqlite3.connect('joukkue.db')
        #connection = sqlite3.connect('/home/pi/JoukkueBot/joukkue.db')
    c = connection.cursor()
    c.execute('SELECT * FROM Quotes')
    quotes = c.fetchall()
    context = {}
    context['quotes'] = {}
    for quote in quotes:
        context['quotes'][quote[0]] = quote[1]
    
    return render(request, "quotes.html", context)
