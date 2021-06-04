from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    image = models.ImageField( upload_to='images/')
    # title = models.ForeignKey(User, on_delete=models.CASCADE)
    #I think the system will be such a way that those who will be able to comment will be logged unto the system
    #so difinitely if will affect the users

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField( upload_to='images/')
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField()
    comments = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        