from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age=models.IntegerField(default=0)
    address=models.TextField(max_length=1000)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
