from django.contrib import admin
from .models import Comment, Image, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=['title','comments']


admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Blog, BlogAdmin)

# Register your models here.
