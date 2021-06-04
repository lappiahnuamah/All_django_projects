
from django.urls import path
from . import views

# app_name = 'project'

urlpatterns = [
    path('', views.all_project, name='all_project'),
    path('<int:project_id>/', views.detail, name='detail'),
]