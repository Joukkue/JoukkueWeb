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

@login_required
def view2(request):
    if request.user.username == "Valtteri":
        return render(request, 'view2.html')
    else:
        return render(request, 'error.html')

def clue2(request):
    return render(request, 'clue2.html')