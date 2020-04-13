from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'search.html')


def booking_request(request):
    return HttpResponse("<h1>hello sachin")
