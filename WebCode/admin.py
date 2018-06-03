from django.contrib import admin

from WebCode.models import Quote, Levels, TelegramUser, TelegramChat

admin.site.register(TelegramUser)
admin.site.register(Quote)
admin.site.register(Levels)
admin.site.register(TelegramChat)