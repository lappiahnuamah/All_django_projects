from django.shortcuts import render, get_object_or_404
from .models import Blog

def index_blog(request):
    blogs = Blog.objects.order_by('-date')
    context = {
        'blogs':blogs
    }
    return render(request, 'index_blog.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'blog_detail.html', context)
