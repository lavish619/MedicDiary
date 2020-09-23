from django.db import models

class patient_details(models.Model):
    usertype=models.CharField(max_length=100,default="patient")
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
  
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
  
    auth_key=models.CharField(max_length=100,default="123")


class notes(models.Model):
    username_p=models.CharField(max_length=100)
    description=models.TextField(max_length=10000)