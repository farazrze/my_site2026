from django.shortcuts import render, get_object_or_404
from blog.models import Post




"""     first way:
def blog_home(request,cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, "blog/home.html", context)
"""

# second way:

def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_name') != None:
        posts = posts.filter(author__username=kwargs['author_name'])
    context = {'posts': posts}
    return render(request, "blog/home.html", context)



def blog_single(request,pid):
    post=get_object_or_404(Post,id=pid,status=1)
    context={"post":post}
    return render(request,"blog/single.html",context)


