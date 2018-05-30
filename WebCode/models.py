from django.db import models

class TelegramChat(models.Model):
    chatid = models.CharField(max_length=64)
    chatName = models.CharField(max_length=64)

class TelegramUser(models.Model):
    userid = models.CharField(max_length=64)
    username = models.CharField(max_length=64)

class Quote(models.Model):
    quote = models.CharField(max_length=256)
    tag = models.CharField(max_length=64)
    userid = models.ForeignKey('TelegramUser', on_delete=models.PROTECT, )

class Levels(models.Model):
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    userid = models.ForeignKey('TelegramUser', on_delete=models.PROTECT,)
    chatName = models.ForeignKey(TelegramChat, on_delete=models.PROTECT,)

