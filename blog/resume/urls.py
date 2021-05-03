from django.urls import path
from resume import views
# from .views import PostListView
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    # path('blog/', PostListView.as_view(), name='blog')
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
]