from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'blog', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name','email', 'body')


admin.site.register(Comment, CommentAdmin)
