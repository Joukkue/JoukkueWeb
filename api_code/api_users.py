from django.http import HttpResponse, JsonResponse
from WebCode.models import Quote, TelegramUser, Levels, TelegramChat

def update(request):
    if request.method == 'POST':
        #Update user
        try:
            user = TelegramUser.objects.get(userid=request.POST.get("userid"))
        except:
            user = None
        if user is None:
            u = TelegramUser(userid=request.POST.get("userid"), username=request.POST.get("username"))
            u.save()
        else:
            user.username = request.POST.get("username")
            user.save()

        # Update chats
        try:
            chat = TelegramChat.objects.get(chatid=request.POST.get('chatid'))
        except:
            chat = None
        if chat is None:
            c = TelegramChat(chatid=request.POST.get('chatid'), chatName=request.POST.get('chatname'))
            c.save()
        else:
            chat.chatName = request.POST.get('chatname')
            chat.save()


        #Update Levels
        user = TelegramUser.objects.get(userid=request.POST.get("userid"))
        try:
            status = Levels.objects.get(userid=user)
        except:
            status = Levels(exp=0,level=0,userid=user,chatid=chat)

        if status.exp > status.level * 100:
            status.level += 1
            status.exp = 0
            status.save()
        else:
            status.exp += 10
            status.save()

    return HttpResponse("Updated")