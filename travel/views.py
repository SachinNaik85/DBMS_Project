from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logged_in(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'naiksachin8585@gmail.com' and password == 'sachin888':
        return render(request, 'index.html')
    else:
        return render(request, 'login.html',  {'message' : 'Invalid credentials'})


def signup(request):
    return render(request, 'signin.html')


def signed_up(request):
    return render(request, 'index.html')


def search_place(request):
    return render(request, 'search.html')