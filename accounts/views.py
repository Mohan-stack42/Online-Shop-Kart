# accounts/models.py - Keep empty, we use Django User!
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created! Login now!')
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong username or password!')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# Create your views here.
