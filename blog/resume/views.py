from django.shortcuts import render
from .models import Resume, Post
# from django.views.generic import ListView
# from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>This is my Home Page</h1>')

def home(request):
    return render(request, 'resume/home.html')

def about(request):
    resume = Resume.objects.get(pk=2)
    return render(request, 'resume/about.html', {"resume": resume})

def blog(request):
    context  =  {
        'posts': Post.objects.all()
    }
    return render(request, 'resume/blog.html', context)

# class PostListView(ListView):
#     model = Post
#     template_name = 'resume/blog.html'
#     context_object_name = 'posts'

#     ordering = ['-date']

def contact(request):
    return render(request, 'resume/contact.html')

def portfolio(request):
    return render(request, 'resume/portfolio.html')