from django.urls import path,include
from . views import *

app_name="blog"

urlpatterns = [
    path("",blog_home,name="home_blog"),
    path("<int:pid>",blog_single,name="single_blog"),
    path("category/<str:cat_name>",blog_category,name="category_blog"),
]