from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def posts():
    return Post.objects.filter(status=1)


@register.filter
def snippet(value, arg=20):
    return value[:int(arg)]


@register.inclusion_tag("post_blog.html")
def latestpost():
    posts=Post.objects.filter(status=1).order_by("update_date")
    return {"posts":posts}
