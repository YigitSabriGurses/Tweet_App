from django.shortcuts import render , redirect
from . import models
from django.urls import reverse , reverse_lazy
from Tweet_App.forms import AddTweetForm , AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


def ListTweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"Tweets": all_tweets}
    return render(request, "Tweet_App/ListTweet.html", context = tweet_dict)


@login_required(login_url="/login")
def AddTweet(request):
    if request.POST:
        message = request.POST["message"]
        models.Tweet.objects.create(username=request.user , message=message)
        return redirect(reverse ('Tweet_App:ListTweet'))
    else:
        return render(request, "Tweet_App/AddTweet.html")


def AddTweetByForm(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname = nickname , message= message)
            return redirect(reverse('Tweet_App:addtweetbyform'))
        else:
            print("error in form")
            return render(request,"Tweet_App/addtweetbyform.html" , context={"form" : form})
    else:
        form = AddTweetForm()
        return render(request,"Tweet_App/addtweetbyform.html" , context={"form" : form})
    

def addtweetbymodelform(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname = nickname , message= message)
            return redirect(reverse('Tweet_App:ListTweet'))
        else:
            print("error in form")
            return render(request,"Tweet_App/addtweetbymodelform.html" , context={"form" : form})
    else:
        form = AddTweetModelForm()
        return render(request,"Tweet_App/addtweetbymodelform.html" , context={"form" : form})
    
@login_required
def DeleteTweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("Tweet_App:ListTweet")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


