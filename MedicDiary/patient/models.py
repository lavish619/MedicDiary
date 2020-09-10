from django.db import models

class patient_details(models.Model):
    usertype=models.CharField(max_length=100,default="patient")
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    bgroup=models.CharField(max_length=50)
    dob =models.CharField(max_length=100)
    address=models.TextField(max_length=1000)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
