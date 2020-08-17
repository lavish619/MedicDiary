from django.shortcuts import render
from django.http import HttpResponse
from .models import details
from .models import register_patient
from .models import register_doctor
from .models import Reports

# Create your views here.
def index(request):
    return render(request,'pract/index.html')



def register_patients(request):
   
    new_patient=register_patient()
    new_patient.patient_username=request.POST.get("patient_username")
    new_patient.patient_name=request.POST.get("patient_name")
    new_patient.patient_age=request.POST.get("patient_age")
    new_patient.patient_address=request.POST.get("patient_address")
    new_patient.patient_contact=request.POST.get("patient_contact")
    new_patient.password_share=request.POST.get("password_share")
    new_patient.password=request.POST.get("password")
    new_patient.save()
    
   
    return render(request,'pract/index.html')


def register_doctors(request):
    
    new_doctor=register_doctor()
    new_doctor.doctor_username=request.POST.get("doctor_username")
    new_doctor.doctor_name=request.POST.get("doctor_name")
    new_doctor.doctor_contact=request.POST.get("doctor_contact")
    new_doctor.password=request.POST.get("password")
    new_doctor.save()
    
   
    return render(request,'pract/index.html')

def logincheckDoctor(request):
    
    Uname=request.POST.get("username","")
    password=request.POST.get("password","")
    if len(register_doctor.objects.filter(doctor_username=Uname))!=0:
        person=register_doctor.objects.get(doctor_username=Uname)
        if person.password == password:
            print("success")
        else:
            print("fail")
        return render(request,'pract/doctor.html')
    else:
        print("not found")
        return render(request,'pract/loginDoctor.html')
    

def logincheckPatient(request):
    
    Uname=request.POST.get("username","")
    password=request.POST.get("password","")
    if len(register_patient.objects.filter(patient_username=Uname))!=0:
        person=register_patient.objects.get(patient_username=Uname)
        if person.password == password:
            print("success")
            allReports=Reports.objects.filter(patient_username=request.POST.get("username"))
            # print(allReports)
            return render(request,"pract/patient.html",{"reports":allReports})
            
        else:
            print("fail")
            return render(request,'pract/loginPatient.html')
        
    else:
        print("not found")
        return render(request,'pract/loginPatient.html')
    
def openPatProfCheck(request):
    
    Uname=request.POST.get("patient_username","")
    security=request.POST.get("security","")
    if len(register_patient.objects.filter(patient_username=Uname))!=0:
        person=register_patient.objects.get(patient_username=Uname)
        if person.password_share == security:
            allReports=Reports.objects.filter(patient_username=request.POST.get("patient_username"))
            # print(allReports)
            return render(request,"pract/patientDoc.html",{"reports":allReports})
            
            # print("success")
              
        else:
            print("fail")
            return render(request,'pract/loginPatient.html')
          
    else:
        print("not found")
        return render(request,'pract/loginPatient.html')
    





def loginDoctor (request):
    return render(request,'pract/loginDoctor.html')

def loginPatient (request):
    return render(request,'pract/loginPatient.html')

def addReport(request):
    return render(request,'pract/newReport.html')

def addingReport(request):
    newReport=Reports()
    newReport.doctor_name=request.POST.get("doctor_name")
    newReport.patient_name=request.POST.get("patient_name")
    newReport.patient_username=request.POST.get("patient_username")
    newReport.patient_age=request.POST.get("patient_age")
    newReport.doctor_notes=request.POST.get("doctor_notes")
    newReport.doctor_prescription=request.POST.get("doctor_pres")
    newReport.save()

    allReports=Reports.objects.filter(patient_username=request.POST.get("patient_username"))
    print(allReports)
    return render(request,"pract/patientDoc.html",{"reports":allReports})





    
    