from django.http import HttpResponse, JsonResponse
from WebCode.models import Quote, TelegramUser, Levels, TelegramChat

def update(request):
    if request.method == 'POST':
        #Update user
        user = TelegramUser.objects.get(userid=request.POST.get("userid"))
        if user is None:
            u = TelegramUser(userid=request.POST.get("userid"), username=request.POST.get("username"))
            u.save()
        else:
            user.username = request.POST.get("username")
            user.save()
        #Update Levels
        status = Levels.objects.get(userid=user.userid)
        if status.exp > status.level * 100:
            status.level += 1
            status.exp = 0
            status.save()
        else:
            status.exp += 10
            status.save()
        #Update chats
        chat = TelegramChat.objects.get(chatid=request.POST.get('chatid'))
        if chat is None:
            c = TelegramChat(chatid=request.POST.get('chatid'), chatName=request.POST.get('chatname'))
            c.save()
        else:
            chat.chatName = request.POST.get('chatname')
            chat.save()