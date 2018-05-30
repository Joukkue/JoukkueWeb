from django.http import HttpResponse, JsonResponse
from WebCode.models import Quote, TelegramUser

def getQuote(request, tag):
    q = Quote.objects.get(tag='testi')
    message = q.quote + '\n' + q.userid.username
    context = {'message':message}
    return JsonResponse(context)
    #return HttpResponse(q.userid.userid)

def getQuotes(request):
    q = Quote.objects.all()
    message = "List of all quotes \n"
    for x in q:
        message += x.tag + "\n"
    context = {'message': message}
    return JsonResponse(context)

def addQuote(request):
    if request.method == 'POST':
        q = Quote(userid=request.POST.get("userid"), tag=request.POST.get("tag"), quote=request.POST.get("quote"))
        q.save()

