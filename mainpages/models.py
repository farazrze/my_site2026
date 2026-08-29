from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.name


class newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
