from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def posts():
    return Post.objects.filter(status=1)


@register.filter
def snippet(value, arg=20):
    return value[:int(arg)]