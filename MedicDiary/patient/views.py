from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import patient_details
from .models import patient_details

def patientProfile(request):
    return render(request, 'patient/patient_profile.html')
def patientRecords(request):
    return render(request, 'patient/patient_records.html')

def registerpage(request):
    return render(request,'patient/register.html')

def signup(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        # age=request.POST['age']
        # bgroup=request.POST['bgroup']
        # dob=request.POST['dob']
        # gender=request.POST['gender']
        # address=request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        # mobile=request.POST['mobile']
        # usertype="patient"


        if len(username)>15:
            messages.error(request,'length of username should be less than15')
            return redirect('patient:registerpage')
        
        # new_patient=patient_details()
        # new_patient.fname=fname
        # new_patient.lame=lname
        # new_patient.age=age
        # new_patient.bgroup=bgroup
        # new_patient.dob=dob
        # new_patient.gender=gender
        # new_patient.address=address
        # new_patient.username=username
        # new_patient.email=email
        # new_patient.mobile=mobile

        # new_patient.save()

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        # myuser.age=age
        # myuser.bgroup=bgroup
        # myuser.dob=dob
        # myuser.gender=gender
        # myuser.address=address
        # myuser.mobile=mobile
       
        
        myuser.save()

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
            return HttpResponse('loggedin as patient') 

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