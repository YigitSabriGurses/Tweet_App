from django.urls import path
from . import views

app_name= "Tweet_App"

urlpatterns = [
    path("", views.ListTweet, name="ListTweet"),
    path("addtweet/", views.AddTweet, name="AddTweet"),
    path("addtweetbyform/" , views.AddTweetByForm, name="addtweetbyform"),
    path("addtweetbymodelform/" , views.addtweetbymodelform, name="addtweetbymodelform"),
    path("signup/" , views.SignUpView.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.DeleteTweet, name="deletetweet")
]