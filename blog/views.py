from django.shortcuts import render, get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import Comments_form
from django.contrib import messages


def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_name') != None:
        posts = posts.filter(author__username=kwargs['author_name'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts': posts}
    return render(request, "blog/home.html", context)


def blog_single(request,pid):
    if request.method == "POST":
        my_form = Comments_form(request.POST)
        if my_form.is_valid():
            my_form.save()
            messages.add_message(request,messages.SUCCESS,"your comment submited succesfuly")
        else:
            messages.add_message(request,messages.ERROR,"your comment didnt submited")


    post=get_object_or_404(Post,id=pid,status=1)
    comments = Comment.objects.filter(post=post.id,approve=True)
    my_form= Comments_form()
    context={"post":post,"comments":comments,"form":my_form}

    return render(request,"blog/single.html",context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        if request.GET.get('s'):
            posts = posts.filter(content__contains = request.GET.get('s'))
    context = {"posts":posts}
    return render(request,"blog/home.html",context)
