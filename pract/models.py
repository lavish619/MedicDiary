from django.db import models

# Create your models here.
class details(models.Model):
    username=models.CharField(max_length=50)
    passward=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class report(models.Model):
    doctor_name=models.CharField(max_length=50)
    patient_name=models.CharField(max_length=50)
    patient_age=models.ImageField()
    doctor_diagnosis=models.CharField(max_length=50)
    doctor_notes=models.TextField(max_length=1000)
    doctor_prescription=models.TextField(max_length=1000)
    image=models.ImageField(default="")


class register_patient(models.Model):
    patient_username=models.CharField(max_length=50)
    patient_name=models.CharField(max_length=50)
    patient_age=models.IntegerField()
    patient_contact=models.CharField(max_length=15)
    patient_address=models.CharField(max_length=200)
    password_share=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class register_doctor(models.Model):
    doctor_username=models.CharField(max_length=50)
    doctor_name=models.CharField(max_length=50)
    doctor_contact=models.CharField(max_length=15)
    password=models.CharField(max_length=50)

class Reports(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_username=models.CharField(max_length=50)
    patient_age=models.IntegerField()
    doctor_name=models.CharField(max_length=50)
    doctor_notes=models.TextField(max_length=1000)
    doctor_prescription=models.TextField(max_length=500)
    
