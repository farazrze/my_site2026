from django.urls import path,include
from . views import *

app_name="mainpages"

urlpatterns = [
    path("",index,name="home"),
    path("contact",contact,name="contact"),
    path("about",about,name="about"),
    path("newsletter",newsletter,name="newsletter")
]