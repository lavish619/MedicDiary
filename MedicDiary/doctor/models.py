from django.db import models

# Create your models here.
class doc_details(models.Model):
    usertype=models.CharField(max_length=100,default="doctor")
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
  
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
  
    
class patient_doc_config(models.Model):
    patient_username=models.CharField(max_length=100)
    doctor_username=models.CharField(max_length=100)
    auth_key=models.CharField(max_length=100)

class records(models.Model):
    doctor_username=models.CharField(max_length=100,default="sdk")
    patient_username=models.CharField(max_length=100,default="skdjks")
    diagnosis=models.CharField(max_length=100)
    doctor_notes=models.TextField(max_length=1000)
    medications=models.TextField(max_length=1000)