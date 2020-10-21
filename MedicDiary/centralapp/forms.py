from django import forms
from django.contrib.auth.models import User
from .models import PatientProfile,DoctorProfile,PatientVitals

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('name','age','address','phone','emergency_contact','profession','gender','profile_pic','Aadhar_Number')

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ('name','phone','Specialisation','City','Registration_Number','Registration_Council','Registration_year','Degree','College','Year_of_completion','Medical_registration_proof','Current_place_of_work','Gender','Profile_pic','Aadhar_Number')

class PatientVitalsForm(forms.ModelForm):
    class Meta:
        model = PatientVitals
        fields = ('Height_in_Centimeters','Weight_in_kilograms','Allergies','Smoker_or_not','Chronic_conditions')
