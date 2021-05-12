from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"blog_id": self.id})
    
    

