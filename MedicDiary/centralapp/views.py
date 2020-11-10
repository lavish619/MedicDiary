from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from patient.models import PatientProfile
from doctor.models import DoctorProfile
# from patient.models import PatientProfile
# import requests
# from bs4 import BeautifulSoup


def mainpage(request):
    # page = request.get('')
    # soup = BeautifulSoup(page.text,'html.parser')
    # https://www.niams.nih.gov/health-topics/all-diseases
    # https://www.cdc.gov/diseasesconditions/index.html
    # https://www.pinehurstmedical.com/internalmedicine/internal-medicine-diseases-disorders-a-syndromes/
    # https://familydoctor.org/diseases-and-conditions/
    return render(request,'centralapp/mainpage.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            usert =3
            # if request.user.patient.usertype=="1":
            if PatientProfile.objects.filter(patient = request.user):
                isuser = PatientProfile.objects.filter(patient = request.user)
                usert = [int(each.usertype) for each in isuser][0]
            elif DoctorProfile.objects.filter(doctor=request.user):
                isuser = DoctorProfile.objects.filter(doctor=request.user)
                usert = [int(each.usertype) for each in isuser][0]
            # usertype = [int(each.usertype) for each in isuser][0]
            # usertype = [int(each.usertype) for each in isuser]
            if usert==1:
                # return render(request,'centralapp/temp.html',{'isuser':isuser,'usert':usert})
                return redirect('patient:patientProfile')
            elif usert==2:
                return redirect('doctor:doctorProfile')
            # return render(request,'centralapp/temp.html', {'isuser':isuser,'usertype':usertype})
        # elif request.user.doctor.usertype=="2":
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('login')
    return render(request,'centralapp/login.html')

# uniquetogether



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
