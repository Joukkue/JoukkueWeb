from django.urls import path
from api_code.api_quotes import *
from api_code.api_users import *

urlpatterns = [
    path('api/quotes/random', randomQuote),
    path('api/quotes/<str:tag>', getQuote),
    path('api/quotes', getQuotes),
    path('api/addquote', addQuote),
    path('api/update', update)
]
