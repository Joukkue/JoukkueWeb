from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view1(request):
    if request.user.username == "Jenna":
        return render(request, 'view1.html')
    else:
        return render(request, 'error.html')

def clue(request):
    return render(request, 'clue1.html')