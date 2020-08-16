from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    return render(request,'centralapp/mainpage.html')

def about_us(request):
    return render(request,'centralapp/about_us.html')
