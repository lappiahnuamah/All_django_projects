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
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html', {"resume": resume})

def blog(request):
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        posts = posts.filter(title__icontains = item_name)
    # context  =  {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'resume/blog.html', {'posts': Post.objects.all().order_by('-date')})

# class PostListView(ListView):
#     model = Post
#     template_name = 'resume/blog.html'
#     context_object_name = 'posts'

#     ordering = ['-date']

def contact(request):
    return render(request, 'resume/contact.html')

def portfolio(request):
    return render(request, 'resume/portfolio.html')