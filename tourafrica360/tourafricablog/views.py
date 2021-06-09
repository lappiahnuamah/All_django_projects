from django.core import paginator
from django.shortcuts import redirect, render , get_object_or_404
from .models import Image, Blog
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_trail')
def index(request):
    # comments = Comment.objects.all()
    images = Image.objects.all()
    context = {
        # 'comments':comments,
        'images':images,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login_trail')
def about(request):
    return render(request, 'about.html')



@login_required(login_url='login_trail')
def blog(request):
    # comments = Comment.objects.all()
    object_list= Blog.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        blogs = paginator.page(1)
    except EmptyPage:
        #If page is out of range deliver last page of results
        blogs = paginator.page(paginator.num_pages)
         
    context = {
        # 'comments':comments,
        'page':page,
        'blogs':blogs,
    }

    return render(request, 'blog.html', context)




def blog_detail(request, year, month, day, post):
    blog = get_object_or_404(Blog, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog_detail.html', {'blog':blog})






@login_required(login_url='login_trail')
def contact(request):
    return render(request, 'contact.html')