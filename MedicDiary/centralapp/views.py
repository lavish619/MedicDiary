from django.shortcuts import render,redirect
from django.http import HttpResponse
# import requests
# from bs4 import BeautifulSoup
# Create your views here.

def mainpage(request):
    # page = request.get('')
    # soup = BeautifulSoup(page.text,'html.parser')
    # https://www.niams.nih.gov/health-topics/all-diseases
    # https://www.cdc.gov/diseasesconditions/index.html
    # https://www.pinehurstmedical.com/internalmedicine/internal-medicine-diseases-disorders-a-syndromes/
    # https://familydoctor.org/diseases-and-conditions/


    return render(request,'centralapp/mainpage.html')

def About_us(request):
    return render(request,'centralapp/about_us.html')
def Cancer(request):
    return render(request,'centralapp/cancer.html')
def Covid_19(request):
    return render(request,'centralapp/Covid_19.html')
def Diabetes(request):
    return render(request,'centralapp/diabetes.html')
def FAQS(request):
    return render(request,'centralapp/faqs.html')
def Heart_disorder(request):
    return render(request,'centralapp/heart_disorder.html')
def doc_how_to_use(request):
    return render(request,'centralapp/how_to_use_Doctor.html')
def patients_how_to_use(request):
    return render(request,'centralapp/how_to_use_User.html')
def Hypertension(request):
    return render(request,'centralapp/hypertension.html')
def Inside_health_records(request):
    return render(request,'centralapp/inside_health_records.html')
def Aids(request):
    return render(request,'centralapp/aids.html')

