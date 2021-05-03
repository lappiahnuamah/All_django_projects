from django.shortcuts import render
from .models import Resume, Post
from django.db.models import Q
from .forms import ContactMe
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
        posts = posts.objects.filter(Q(title__icontains = item_name))
    return render(request, 'resume/blog.html', posts)


# class PostListView(ListView):
#     model = Post
#     template_name = 'resume/blog.html'
#     # context_object_name = 'posts'

#     ordering = ['-date']

    # return render(request, 'resume/blog.html', )
        # return object_list

    # def search(request):
    # if request.method == 'GET':
    #     form = LocForm(request.POST)
    #     if form.is_valid():
    #         search_query = request.GET.get('search_box', None)
    #         if search_query:
    #             FirstLoc_list_obj = FirstLoc_List.objects.filter(address__icontains=search_query)
    #             SecondLoc_list_obj= SecondLoc_list.objects.filter(address__icontains=search_query)


# def contact(request):
#     return render(request, 'resume/contact.html')

def portfolio(request):
    return render(request, 'resume/portfolio.html')

def contact(request):
    contact = ContactMe()
    return render(request, 'resume/contact.html', {'contact':contact})