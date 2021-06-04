from django.shortcuts import redirect, render
from .models import Comment, Image, Blog
from .forms import CommentForm
# from django.views.generic import ListView, DetailView,
from django.urls import reverse


from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_trail')
def index(request):
    comments = Comment.objects.all()
    images = Image.objects.all()
    context = {
        'comments':comments,
        'images':images,
    }
    return render(request, 'index.html', context)

@login_required(login_url='login_trail')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login_trail')
def blog(request):
    comments = Comment.objects.all()
    blogs = Blog.objects.all()
    context = {
        'comments':comments,
        'blogs':blogs,
    }
    return render(request, 'blog.html', context)

# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'post_detail.html'

#     forms = CommentForm
    
#     def post(self, request, *args, **kwargs):
#         forms = CommentForm(request.POST)
#         if forms.is_valid():
#             post = self.get_object()
#             forms.instance.user = request.user
#             forms.instance.post = post
#             forms.save()
#         return redirect(reverse('blog',))



@login_required(login_url='login_trail')
def contact(request):
    return render(request, 'contact.html')