from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePageView(response):
    return HttpResponse('Hello World')
