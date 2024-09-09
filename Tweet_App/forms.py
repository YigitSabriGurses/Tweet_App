from django import forms
from django.forms import ModelForm
from Tweet_App.models import Tweet


class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label= "nickname" , max_length=50)
    message_input = forms.CharField(label= "message" , max_length=100 , widget=forms.Textarea(attrs={"class":"tweetmessage"}))



class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username" , "message"]