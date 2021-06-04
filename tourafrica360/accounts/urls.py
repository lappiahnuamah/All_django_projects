from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.login_trail, name="login_trail"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('register/', views.register_trail, name="register_trail"),
]