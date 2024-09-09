from django.contrib import admin
from Tweet_App.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    fields = ["nickname" , "message"]


admin.site.register(Tweet, TweetAdmin)
