from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to="blog/",default="blog/default.jpg")
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    publish_date = models.DateField(null=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    counter_view = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)


    class Meta:
        ordering = ["-create_date"]
    def __str__(self):
        return "{} {}".format(self.title,self.id)