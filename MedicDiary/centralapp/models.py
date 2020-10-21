from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(blank=False)
    address = models.TextField(max_length=500, blank=False)
    phone = models.CharField(max_length=40, blank=False)
    emergency_contact = models.CharField(max_length=40, blank=False)
    profession = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    profile_pic = models.ImageField(default = 'patients_profile_pictures/defaultprofilepic.jpg', upload_to = 'patients_profile_pictures')
    Aadhar_Number= models.IntegerField(blank=False)

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    Gender = models.CharField(max_length=30)
    Specialisation = models.CharField(max_length=30)
    phone = models.CharField(max_length=40, blank=False)
    City = models.CharField(max_length=30)
    Registration_Number = models.CharField(max_length=40, blank=False)
    Registration_Council = models.CharField(max_length=100, blank=False)
    Registration_year = models.IntegerField(blank=False)
    Degree = models.CharField(max_length=100, blank=False)
    College = models.CharField(max_length=100, blank=False)
    Year_of_completion = models.IntegerField()
    Profile_pic = models.ImageField(default = 'patients_profile_pictures/defaultprofilepic.jpg', upload_to = 'doctors_profile_pictures')
    Medical_registration_proof = models.FileField(upload_to = 'DoctorRegProofs')
    Current_place_of_work = models.CharField(max_length=30)
    Aadhar_Number= models.IntegerField(blank=False)

class PatientVitals(models.Model):
    Height_in_Centimeters = models.CharField(max_length=100, blank=False)
    Weight_in_kilograms = models.CharField(max_length=100, blank=False)
    Allergies = models.TextField(max_length=30)
    Smoker_or_not = models.CharField(max_length=30)
    Chronic_conditions = models.CharField(max_length=30)
