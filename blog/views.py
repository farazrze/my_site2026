from django.shortcuts import render

def blog_home(request):
    return render(request,"blog/home.html")


def blog_single(request):
    context={"title":"faraz firs try","body":"this is a first try for add context to this fucking travel site","aouthor":"faraz rze"}
    return render(request,"blog/single.html",context)