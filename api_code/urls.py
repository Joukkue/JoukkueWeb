from django.urls import path
from api_code.api_quotes import *

urlpatterns = [
    path('api/quotes/<str:tag>', getQuote),
    path('api/quotes', getQuotes),
    path('api/addquote', addQuote),
]
