from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=1024, blank=False)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    report = models.CharField(max_length=1024, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment