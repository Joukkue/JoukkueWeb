from django.db import models


class TelegramChat(models.Model):
    chatid = models.CharField(max_length=64)
    chatName = models.CharField(max_length=64)

    def __str__(self):
        return 'Chat: ' + self.chatName


class TelegramUser(models.Model):
    userid = models.CharField(max_length=64)
    username = models.CharField(max_length=64)

    def __str__(self):
        return 'User: ' + self.username


class Quote(models.Model):
    quote = models.CharField(max_length=256)
    tag = models.CharField(max_length=64, unique=True)
    userid = models.ForeignKey('TelegramUser', on_delete=models.PROTECT, )

    def __str__(self):
        return 'Quote: ' + self.tag


class Levels(models.Model):
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    userid = models.ForeignKey('TelegramUser', on_delete=models.PROTECT,)
    chatid = models.ForeignKey('TelegramChat', on_delete=models.PROTECT,)

    def __str__(self):
        return 'Level: ' + self.userid.username + ' ' + self.chatid.chatName

