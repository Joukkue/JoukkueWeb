from django.http import HttpResponse, JsonResponse
from WebCode.models import Quote, TelegramUser
from django.db import IntegrityError

def getQuote(request, tag):
    q = Quote.objects.get(tag=tag)
    message = q.quote + '\n@' + q.userid.username
    context = {'message':message}
    return JsonResponse(context)


def getQuotes(request):
    q = Quote.objects.all()
    message = "List of all quotes \n"
    for x in q:
        message += x.tag + "\n"
    context = {'message': message}
    return JsonResponse(context)


def addQuote(request):
    if request.method == 'POST':
        try:
            q = Quote(userid=TelegramUser.objects.get(userid=request.POST.get("userid")), tag=request.POST.get("tag"), quote=request.POST.get("quote"))
            q.save()
            message = "Quote added succesfully"
            context = {'message': message}
            return JsonResponse(context)
        except IntegrityError as err:
            if 'unique constraint' in err.args[0]:
                message = "Quote with this tag already exists"
            else:
                message = "Something went horribly horribly wrong"
            context = {'message': message}
            return JsonResponse(context)

