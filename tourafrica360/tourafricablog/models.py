from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    image = models.ImageField( upload_to='images/')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # comments = models.ForeignKey(Comment, blank=True, on_delete=models.CASCADE)
    upvotes= models.PositiveIntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    objects = models.Manager() #the default manager
    published = PublishedManager()  # the dahl-specific manager


    class Meta:
        ordering = ['-publish',]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.publish.year,
                                            self.publish.strftime('%m'),
                                            self.publish.strftime('%d'),
                                            self.slug])
    
        