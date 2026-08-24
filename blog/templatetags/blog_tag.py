from django import template
from blog.models import Post,Category

register = template.Library()


@register.simple_tag
def posts():
    return Post.objects.filter(status=1)


@register.filter
def snippet(value, arg=20):
    return value[:int(arg)]


@register.inclusion_tag("blog/post_blog.html")
def latestpost():
    posts=Post.objects.filter(status=1).order_by("update_date")
    return {"posts":posts}

@register.inclusion_tag("blog/cat_blog.html")
def category():
    post = Post.objects.filter(status=1)
    cat = Category.objects.all()
    cat_dic = {}
    for name in cat:
        cat_dic[name]= post.filter(category=name).count()
    return {"categoris":cat_dic}