from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import *

def home(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
            return HttpResponseRedirect('/home')

    return render(request, 'home/home.html')

def user_signup(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            return HttpResponseRedirect('/login')
        elif 'signup' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/home')
    else:
        form = RegistrationForm()
        
    return render(request, 'home/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home')
                else:
                    form.add_error(None, 'Invalid username or password')

        elif 'signup' in request.POST:
            return HttpResponseRedirect('/signup')
    else:
        form = LoginForm()

    return render(request, 'home/login.html', {'form': form})

def settings(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
            return HttpResponseRedirect('/home')
    return render(request, 'home/settings.html')