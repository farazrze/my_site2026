from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=True)
    publish_date = models.DateField(null=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    counter_view = models.IntegerField(default=0)
    class Meta:
        ordering = ["-create_date"]
    def __str__(self):
        return "{} {}".format(self.title,self.id)