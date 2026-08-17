from django.shortcuts import render
from blog.models import Post




def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, "blog/home.html", context)


def blog_single(request):
    context={"title":"faraz firs try","body":"this is a first try for add context to this fucking travel site","aouthor":"faraz rze"}
    return render(request,"blog/single.html",context)