from django.urls import path,include
from . views import *

app_name="blog"

urlpatterns = [
    path("",blog_home,name="home_blog"),
    path("single",blog_single,name="single_blog"),
]