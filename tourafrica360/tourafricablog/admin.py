from django.contrib import admin
from .models import Image, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy='publish'
    ordering = ['status', 'publish']


# admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Blog, BlogAdmin)

# Register your models here.
