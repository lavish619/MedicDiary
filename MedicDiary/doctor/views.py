from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import DoctorRegisterForm, DoctorProfileForm
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import DoctorProfile
from django.views import View


=======
from .models import DoctorProfile,PatientDocConfig
from patient.models import PatientProfile,PatientVitals,LabReports,Records
import datetime
>>>>>>> bf7e68a06a7bf559c384b3a296ce250729715e75
def doctorRegister(request):
    if request.method =='POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # return redirect('login')
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            usertype = 2
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('doctor:create_doctorprofile')
    else:
        form = DoctorRegisterForm()
    return render(request,'doctor/doctorRegister.html',{'form':form})

@login_required
def create_doctorprofile(request):
    if request.method =='POST':
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.doctor = request.user
            doctor.save()
            # form.doctor = request.user
            # form.save()
            return redirect('doctor:doctorProfile')
    else:
        form = DoctorProfileForm()
    return render(request,'doctor/doctor-profile-create.html',{'form':form})


@login_required
def doctorProfile(request):
    profile = DoctorProfile.objects.get(doctor=request.user)
    
    return render(request, 'doctor/doctor_profile.html',{'profile':profile})

<<<<<<< HEAD
# @login_required
# def PatientList(request):
#     # listed = Mypatients.objects.get(doctorp = request.user).mypatientlist
#     # if len(listed) ==0:
#         # return HttpResponse("emply:(")
#     # patientsl = PatientProfile.objects.getall()
#
#     return render(request, 'doctor/mylist.html',{'patientl':patientl})
=======
@login_required
def PatientList(request):
    # listed = Mypatients.objects.get(doctorp = request.user).mypatientlist
    # if len(listed) ==0:
        # return HttpResponse("emply:(")
    # patientsl = PatientProfile.objects.getall()
    Patient_list=PatientProfile.objects.filter()


    return render(request, 'doctor/patientList.html',{'patientl':Patient_list})


@login_required
def pat_profile(request,p):
    print(p)
    subject=PatientProfile.objects.filter(id=p)
    pat_vitals=PatientVitals.objects.filter(id=p)

    return render(request,'doctor/patient_records_in_doc.html',{'subject':subject,"vitals":pat_vitals[0]})

@login_required
def newReport(request,p):
    doctor=DoctorProfile.objects.filter(doctor=request.user)[0]
    patient=PatientProfile.objects.filter(id=p)[0]
    date=str(datetime.datetime.now()).split(" ")[0]
    
    obj={'doctor_name':doctor.name,'patient_name':patient.name,'date':date,"docid":doctor.id,"patid":patient.id}
    return render(request,'doctor/report.html',{'details':obj})

@login_required
def addReport(request):
    if request.method=="POST":
        new_record=Records()
        new_record.date=str(datetime.datetime.now()).split(" ")[0]
        new_record.diagnosis=request.POST['diagnosis']
        new_record.doctor_name=request.POST['doctor_name']
        new_record.Symptoms=request.POST['symptoms']
        new_record.medication=request.POST['medication']
        new_record.patient_id=request.POST['patid']
        new_record.doctor_id=request.POST['docid']
        new_record.additional_precautions=request.POST['additional_precautions']
        new_record.save()
        addr='doctor:pat_profile/'+ str(request.POST['patid'])

        return redirect('/pat_profile/'+ str(request.POST['patid']))

@login_required
def addPatient(request):
    patient_id=request.POST['patient_id']
    accesscode=request.POST['patient_id']
    if len(PatientProfile.objects.filter(id=patient_id))==0:
        return redirect('/PatientList/')
    else:
        check_pat=PatientProfile.objects.filter(id=patient_id)[0]
        if check_pat.access_code==accesscode:
            new_config=PatientDocConfig()
            new_config.patient_id=patient_id
            new_config.doctor_id=request.user.id
            new_config.access_code=accesscode
            new_config.save()
        else:
            return redirect('/PatientList/')

>>>>>>> bf7e68a06a7bf559c384b3a296ce250729715e75



# @login_required
# class mypatients(View):
#     def get(self,request):
#         return render(request, 'doctor/temp.html',{})






















# ========================================================================
# ========================================================================

#
# from .models import doc_details,patient_doc_config,records
# from django.contrib.sessions.models import Session
# from patient.models import patient_details
#
# # Create your views here.
# def doctor_profile(request):
#     return render(request,'doctor/doctor_profile.html')
#
# def doctorRecords(request):
#     return render(request, 'doctor/doctor_records.html')
#
# def registerpage(request):
#     return render(request,'doctor/register.html')
#
#
#
#
# def signup(request):
#     if request.method=="POST":
#         fname=request.POST['fname']
#         lname=request.POST['lname']
#
#         username=request.POST['username']
#         password=request.POST['password']
#         email=request.POST['email']
#
#
#
#         if len(username)>15:
#             messages.error(request,'length of username should be less than15')
#             return redirect('patient:registerpage')
#
#
#
#         myuser=User.objects.create_user(username,email,password)
#         myuser.first_name=fname
#         myuser.last_name=lname
#
#         new_doc=doc_details()
#         new_doc.lname=lname
#         new_doc.fname=fname
#         new_doc.username=username
#         new_doc.email=email
#         new_doc.save()
#
#         myuser.save()
#
#         newPatient=patient_doc_config()
#         newPatient.patient_username="sample_pusername"
#         newPatient.doctor_username=username
#         newPatient.auth_key=123
#         newPatient.save()
#
#         messages.success(request, 'Form submission successful')
#         return redirect('/')
#
#
#     else :
#         return HttpResponse('404-not found')
#
#
# def loginn(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             print("innn")
#             request.session["username_d"]=username
#             return render(request,'doctor/doctor_profile.html',{"username":username})
#
#         else :
#             print("invalid credentials")
#             return render(request,'centralapp/mainpage.html')
#
#
#         return HttpResponse('login')
#
#
#
#     else:
#         return HttpResponse('404-not found')
#
# def myPatients(request):
#     username=request.session["username_d"]
#     if len(patient_doc_config.objects.filter(doctor_username=username))!=0:
#         pat=patient_doc_config.objects.filter(doctor_username=username)
#         return render(request, 'doctor/mypatients.html',{"patients":pat})
#
#     else :
#         return render(request, 'doctor/mypatients.html',{"patients":"add patients"})
#
#
#     return render(request, 'doctor/mypatients.html',{"username":username})
#
# def doctorProfile(request):
#     return render(request, 'doctor/doctor_profile.html')
#
# def addpatient(request):
#     if request.method=="POST":
#         p_username=request.POST['username']
#         accesscode=request.POST['accesscode']
#
#         if len(patient_details.objects.filter(username=p_username))!=0:
#             pat=patient_details.objects.get(username=p_username)
#             if  pat.auth_key==accesscode:
#
#                 newPatient=patient_doc_config()
#                 newPatient.patient_username=p_username
#                 newPatient.doctor_username=request.session["username_d"]
#                 newPatient.auth_key=accesscode
#                 newPatient.save()
#                 redirect('doctor:myPatients')
#             else :
#                 redirect('doctor:myPatients')
#                 messages.error(request,'access code did not match')
#         else:
#              redirect('doctor:myPatients')
#              messages.error(request,'username does not exist')
#
#
#
#
#         return redirect('doctor:myPatients')
#
#
#     else:
#          return HttpResponse('404-not found')
#
# def doctorRecords(request,p_username):
#     request.session["username_p"]=p_username
#     return render(request, 'doctor/doctor_records.html')
#
#
#
# def addRecord(request):
#     return render(request,'doctor/report.html')
#
# def newReport(request):
#     diagnosis=request.POST['diagnosis']
#     doctor_notes=request.POST['doctor_notes']
#     medications=request.POST['medications']
#
#     new_record=records()
#     new_record.diagnosis=diagnosis
#     new_record.doctor_notes=doctor_notes
#     new_record.medications=medications
#     new_record.doctor_username=request.session["username_d"]
#     new_record.patient_username=request.session["username_p"]
#     new_record.save()
#
#     return redirect('doctor:doctorRecords', p_username=request.session["username_p"])
#
