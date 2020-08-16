from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    return HttpResponse('Hello world!')
