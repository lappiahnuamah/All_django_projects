from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm


from django.contrib import messages



# Create your views here.
def login_trail(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
        return render(request, 'login_trail.html',)


def register_trail(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for "+ user)
                return redirect("login_trail")
        else:
            form = RegisterForm()
        return render(request ,'register_trail.html',{'form':form})


def logoutUser(request):
    logout(request)
    return redirect('login_trail')