# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import * # gives us access to `User`models
from django.contrib import messages # grabs django's `messages` module
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    # If POST, login:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'posts/index.html', {'form': form})

def register(request):
    # If POST, POST:
    form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        user = User.objects.create_user(commit=False)
        user.is_active = False
        user.save()
    return render(request, 'posts/registration.html', {'new user', new_user})


def logged(request):
    # If POST, POST:
    return render(request, 'posts/login.html')

