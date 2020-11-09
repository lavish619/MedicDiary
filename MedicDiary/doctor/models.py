from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from patient.models import PatientProfile

class DoctorProfile(models.Model):

    doctor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    Gender = models.CharField(max_length=30,blank=True)
    Specialisation = models.CharField(max_length=30)
    phone = models.CharField(max_length=40, blank=False, help_text='10 digit Mobile Number')
    City = models.CharField(max_length=30)
    Registration_Number = models.CharField(max_length=40, blank=False)
    Registration_Council = models.CharField(max_length=100, blank=False)
    Registration_year = models.IntegerField(blank=False)
    Degree = models.CharField(max_length=100, blank=False)
    College = models.CharField(max_length=100, blank=False)
    Year_of_completion = models.IntegerField()
    Profile_pic = models.ImageField(default = 'doctors_profile_pictures/defaultprofilepic.jpg', upload_to = 'doctors_profile_pictures')
    Medical_registration_proof = models.FileField(upload_to = 'DoctorRegProofs',blank = True)
    Current_place_of_work = models.CharField(max_length=30)
    Aadhar_Number= models.IntegerField(blank=True, help_text='12 digit unique Aadhar Number')
    usertype = models.IntegerField(default = 2)
    # mypatients = models.ManyToManyField(PatientProfile,through = "pats", related_name = "mypat")
    # mypatient = models.ManyToManyField(PatientProfile, related_name = "mypat")

    def __str__(self):
        return self.name

# class Mypatients(models.Model):
#
#     doctorp = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
#     # mypatientlist = models.ManyToManyField(PatientProfile)
#     # patient.objecs.getall()
#
#
class PatientDocConfig(models.Model):
    doctor_id=models.IntegerField(blank=False)
    
    access_code=models.IntegerField(blank=False)

    # doctorp = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete= models.CASCADE)
    # mypatientlist = models.ManyToManyField(PatientProfile)
    # patient.objecs.getall()
# tablename.relationname.getall
# class pats(models.Model):
#     patconfig = models.ForeignKey(PatientProfile,on_delete= models.CASCADE)
#     docconfig = models.ForeignKey(DoctorProfile,on_delete= models.CASCADE)
#
#     class Meta:
#         unique_together = ('patconfig', 'docconfig')













# =============================================================================================
# =============================================================================================
# Create your models here.
# class doc_details(models.Model):
#     usertype=models.CharField(max_length=100,default="doctor")
#     fname=models.CharField(max_length=100)
#     lname=models.CharField(max_length=100)
#
#     username=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
#
#
# class patient_doc_config(models.Model):
#     patient_username=models.CharField(max_length=100)
#     doctor_username=models.CharField(max_length=100)
#     auth_key=models.CharField(max_length=100)
#
# class records(models.Model):
#     doctor_username=models.CharField(max_length=100,default="sdk")
#     patient_username=models.CharField(max_length=100,default="skdjks")
#     diagnosis=models.CharField(max_length=100)
#     doctor_notes=models.TextField(max_length=1000)
#     medications=models.TextField(max_length=1000)
