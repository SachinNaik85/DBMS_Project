from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1 style = "text-align : center; padding-top : 100px ; color : blue;">'
                        'Hello sachin this is search page</h1>')
