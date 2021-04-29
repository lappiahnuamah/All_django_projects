from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30, default="Available")
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=12)
    Email = models.CharField(max_length=30)
    Github = models.CharField(max_length=35)
    Languages = models.CharField(max_length=30)


class Post(models.Model):
    Image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


class ContactForm(models.Model):
    your_name = models.CharField(max_length=30)
    your_email = models.EmailField()
    your_subject = models.CharField(max_length=30)
    your_message = models.TextField()


    