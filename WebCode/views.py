from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from core.utils import get_context_data

@login_required
def home(request):
	context = get_context_data(request)
	return render(request, 'store/home.html', context)



