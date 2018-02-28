from django.shortcuts import render
import sqlite3

def frontpage(request):
    return render(request, "home.html")

def show(request):
    connection = sqlite3.connect('joukkue.db')
    c = connection.cursor()
    c.execute('SELECT * FROM Quotes')
    quotes = c.fetchall()
    context = {}
    context['quotes'] = {}
    for quote in quotes:
        context['quotes'][quote[0]] = quote[1]
    print (context)
    return render(request, "quotes.html", context)
