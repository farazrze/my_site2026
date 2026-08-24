from django.urls import path,include
from . views import *

app_name="blog"

urlpatterns = [
    path("",blog_home,name="home_blog"),
    path("<int:pid>",blog_single,name="single_blog"),
    path("category/<str:cat_name>",blog_home,name="category_blog"),
    path("author/<str:author_name>",blog_home,name="author_blog"),
    path("search/",blog_search,name="search"),
    #path("page/",blog_home,name="page")
]