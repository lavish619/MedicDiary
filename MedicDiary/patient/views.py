from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import patient_details
import random
import string

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string is:", result_str)


def registerpage(request):
    return render(request,'patient/register.html')

def signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
       
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
       

        if len(username)>15:
            messages.error(request,'length of username should be less than15')
            return redirect('patient:registerpage')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
       
       
        myuser.save()
        print("1")

        patient=patient_details()
        patient.fname=fname
        patient.lname=lname
        patient.username=username
        patient.auth_key=get_random_string(8)
        patient.email=email
        patient.save()
        
        print('2')
        messages.success(request, 'Form submission successful')
        return redirect('/')
       

    else :
        return HttpResponse('404-not found')




def loginn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print("innn")
            return render(request,'patient/patient_profile.html')

        else :
            print("invalid credentials")
            return render(request,'centralapp/mainpage.html')


        return HttpResponse('login')



    else:
        return HttpResponse('404-not found')

def logout(request):
    if request.method=="POST":
        logout(request)
        return render(request,'patient/mainpage.html') 
    return HttpResponse('logout')