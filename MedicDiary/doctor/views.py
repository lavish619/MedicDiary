from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import doc_details,patient_doc_config,records
from django.contrib.sessions.models import Session
from patient.models import patient_details

# Create your views here.
def doctor_profile(request):
    return render(request,'doctor/doctor_profile.html')

def doctorRecords(request):
    return render(request, 'doctor/doctor_records.html')

def registerpage(request):
    return render(request,'doctor/register.html')




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

        new_doc=doc_details()
        new_doc.lname=lname
        new_doc.fname=fname
        new_doc.username=username
        new_doc.email=email
        new_doc.save()

        myuser.save()

        newPatient=patient_doc_config()
        newPatient.patient_username="sample_pusername"
        newPatient.doctor_username=username
        newPatient.auth_key=123
        newPatient.save()

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
            request.session["username_d"]=username
            return render(request,'doctor/doctor_profile.html',{"username":username})

        else :
            print("invalid credentials")
            return render(request,'centralapp/mainpage.html')


        return HttpResponse('login')



    else:
        return HttpResponse('404-not found')

def myPatients(request):
    username=request.session["username_d"]
    if len(patient_doc_config.objects.filter(doctor_username=username))!=0:
        pat=patient_doc_config.objects.filter(doctor_username=username)
        return render(request, 'doctor/mypatients.html',{"patients":pat})

    else :
        return render(request, 'doctor/mypatients.html',{"patients":"add patients"})


    return render(request, 'doctor/mypatients.html',{"username":username})

def doctorProfile(request):
    return render(request, 'doctor/doctor_profile.html')

def addpatient(request):
    if request.method=="POST":
        p_username=request.POST['username']
        accesscode=request.POST['accesscode']

        if len(patient_details.objects.filter(username=p_username))!=0:
            pat=patient_details.objects.get(username=p_username)
            if  pat.auth_key==accesscode:

                newPatient=patient_doc_config()
                newPatient.patient_username=p_username
                newPatient.doctor_username=request.session["username_d"]
                newPatient.auth_key=accesscode
                newPatient.save()
                redirect('doctor:myPatients')
            else :
                redirect('doctor:myPatients')
                messages.error(request,'access code did not match')
        else:
             redirect('doctor:myPatients')
             messages.error(request,'username does not exist')




        return redirect('doctor:myPatients')


    else:
         return HttpResponse('404-not found')

def doctorRecords(request,p_username):
    request.session["username_p"]=p_username
    return render(request, 'doctor/doctor_records.html')



def addRecord(request):
    return render(request,'doctor/report.html')

def newReport(request):
    diagnosis=request.POST['diagnosis']
    doctor_notes=request.POST['doctor_notes']
    medications=request.POST['medications']

    new_record=records()
    new_record.diagnosis=diagnosis
    new_record.doctor_notes=doctor_notes
    new_record.medications=medications
    new_record.doctor_username=request.session["username_d"]
    new_record.patient_username=request.session["username_p"]
    new_record.save()

    return redirect('doctor:doctorRecords', p_username=request.session["username_p"])
