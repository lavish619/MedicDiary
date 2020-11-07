from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import PatientRegisterForm,PatientProfileForm,PatientVitalsForm
from django.contrib.auth.decorators import login_required
from .models import PatientProfile,PatientVitals,Records
from django.contrib.auth import logout
#
# def auth(str):
#     return(hash(str))

# def create_profile(request):
#     form = ProfileForm(request.POST or None)  #class created in forms.py
#     if form.is_valid():
#         form.save()
#         return redirect('centralapp:mainpage')
#     return render(request,'centralapp/profile-create.html',{'form':form})
#
def patientRegister(request):
    if request.method =='POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # return redirect('login')
            user = form.save(commit=False)
            user.usertype= 1
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # email = form.cleaned_data['email']
            # user.AccessCode = hash(email)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient:create_patientprofile')
    else:
        form = PatientRegisterForm()
    return render(request,'patient/patientregister.html',{'form':form})

# @login_required
# def patient_create(request):
#     form = PatientForm()
#     if request.method == 'POST':
#         form = PatientForm(request.POST, request.FILES)
#         if form.is_valid():
#             patient = form.save(commit=False)
#             patient.user = request.user
#             patient.save()
#             return redirect('patient-detail')
#     context = {'form':form}
#     template = 'userinfo/patients/patient-create.html'
#     return render(request, template, context)

@login_required
def create_patientprofile(request):
    if request.method =='POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():

            patient = form.save(commit=False)
            # name = form.cleaned_data['name']
            # patient.AccessCode = hash(name)
            patient.patient = request.user
            patient.save()
            # form.patient = request.user
            # form.save()
            patient=PatientProfile.objects.filter(patient=request.user)[0]
            print(patient.address)
            print(hash(patient.address))
            patient.access_code=hash( str(patient.id) +patient.address)
            patient.save()
            
            return redirect('patient:patientvitals_input')
    else:
        form = PatientProfileForm()
    return render(request,'patient/patient-profile-create.html',{'form':form})

@login_required
def patientvitals_input(request):
    if request.method =='POST':
        form = PatientVitalsForm(request.POST)
        if form.is_valid():
            patientv = form.save(commit=False)
            patientv.patientv = request.user
            patientv.save()
            # form.save()
            return redirect('patient:patientProfile')
    else:
        form = PatientVitalsForm()
    return render(request,'patient/patientvital_info.html',{'form':form})

 
@login_required
def patientProfile(request):
    profile = PatientProfile.objects.get(patient=request.user)
    return render(request, 'patient/patient_profile.html',{'profile':profile})

@login_required
def patientRecords(request):
    vitals = PatientVitals.objects.get(patientv=request.user)
    patient=PatientProfile.objects.filter(patient=request.user)[0]
    all_reports=list(Records.objects.filter(patient_id=patient.id).order_by('id').reverse())
    count=0
    rec=[]
    for r in all_reports:
        if count ==1:
            break
        rec.append(r)
        count=count+1


        for report in rec:
            des=report.medication
            med=des.split(":")
            m_list=[]
            for m in med:
	            dosage=m.split("/")
	            m_list.append(dosage)

            report.medication=m_list



    return render(request, 'patient/patient_records.html',{'vitals':vitals,'Reports':rec})

@login_required 
def labreports(request):
    return render(request, 'patient/labreports.html')

@login_required
def medications(request):
    patient=PatientProfile.objects.filter(patient=request.user)[0]
    all_reports=Records.objects.filter(patient_id=patient.id).order_by('id').reverse()
    
    print(len(all_reports.reverse()))
    for report in all_reports:
        des=report.medication
        med=des.split(":")
        m_list=[]
        for m in med:
	        dosage=m.split("/")
	        m_list.append(dosage)

        report.medication=m_list
        

    return render(request, 'patient/medications.html',{'Reports':all_reports})

@login_required
def editPatient(request):
    patient = get_object_or_404(PatientProfile, patient=request.user)
    # patient = PatientProfile.objects.get(patient=request.user)
    # if request.method == 'POST':
    form = PatientProfileForm(request.POST, request.FILES, instance=patient)
    # if request.method == 'POST':

    if form.is_valid():
        patient = form.save(commit=False)
        patient.patient = request.user
        patient.save()
        return redirect('patient:patientProfile')
    # else:
    #     form = PatientProfileForm()
    return render(request,'patient/patient-profile-edit.html',{'form':form})

@login_required
def editPatientVitals(request):
    patientv = get_object_or_404(PatientVitals, patientv=request.user)
    # if request.method == 'POST':
    form = PatientVitalsForm(request.POST, request.FILES, instance=patientv)
    if form.is_valid():
        patientv = form.save(commit=False)
        patientv.patientv = request.user
        patientv.save()
        return redirect('patient:patientRecords')
    # else:
        # form = PatientVitalsForm()
    return render(request,'patient/patient-vitals-edit.html',{'form':form})


# 
# def logout_view(request):
#     logout(request)
#     return render(r'^logout/$', 'django.contrib.auth.views.logout',
#                           {'next_page': '/successfully_logged_out/'})
#





# ===============================================================
# =================================================================
# ============================================================================

# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
# from django.middleware.csrf import get_token
# # from .forms import RegisterForm, ProfileForm
# # from .models import Profile
# from django.contrib.auth.decorators import login_required
#
#
# from .models import patient_details,notes
# import random
# import string
#
# def get_random_string(length):
#     # Random string with the combination of lower and upper case
#     letters = string.ascii_letters
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     print("Random string is:", result_str)
#
#
# def patientProfile(request):
#     return render(request, 'patient/patient_profile.html')
# def patientRecords(request):
#     return render(request, 'patient/patient_records.html')
#
# def labreports(request):
#     return render(request, 'patient/labreports.html')
# def medications(request):
#     return render(request, 'patient/medications.html')
#
# def registerpage(request):
#     return render(request,'patient/register.html')
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
#         if len(username)>15:
#             messages.error(request,'length of username should be less than15')
#             return redirect('patient:registerpage')
#
#         myuser=User.objects.create_user(username,email,password)
#         myuser.first_name=fname
#         myuser.last_name=lname
#
#
#         myuser.save()
#         print("1")
#
#         patient=patient_details()
#         patient.fname=fname
#         patient.lname=lname
#         patient.username=username
#         patient.auth_key=get_random_string(8)
#         patient.email=email
#         patient.save()
#
#         print('2')
#         messages.success(request, 'Form submission successful')
#         return redirect('/')
#
#
#     else :
#         return HttpResponse('404-not found')
#
#
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
#             request.session["username_p"]=username
#             return render(request,'patient/patient_profile.html')
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
# def logout(request):
#     if request.method=="POST":
#         logout(request)
#         return render(request,'patient/mainpage.html')
#     return HttpResponse('logout')
#
#
# def addnotes(request):
#     if request.user.is_authenticated:
#         user=request.user
#         description=request.POST['description']
#         username= user.username
#         if len(notes.objects.filter(username_p=username))!=0:
#             notes.objects.filter(username_p=username).delete()
#             new_note=notes()
#             new_note.username_p=username
#             new_note.description=description
#             new_note.save()
#         else:
#             new_note=notes()
#             new_note.username_p=username
#             new_note.description=description
#             new_note.save()
#
#
#         return redirect('patient:personalNotes')
#
# def personalNotes(request):
#     csrf_token = get_token(request)
#     csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)
#     if request.user.is_authenticated:
#         user=request.user
#         if len(notes.objects.filter(username_p=user.username))==0:
#             new_note = notes()
#             new_note.username_puser.username
#             new_note.description = 'Add your notes here'
#             new_note.save()
#         note=notes.objects.get(username_p=user.username)
#         return render(request, 'patient/personalNotes.html',{"des":note.description})
#
# # def create_item(request):
# #     form = ItemForm(request.POST or None)  #class created in forms.py
# #     if form.is_valid():
# #         form.save()
# #         return redirect('food:mainpage')
# #     return render(request,'food/item-form.html',{'form':form})
