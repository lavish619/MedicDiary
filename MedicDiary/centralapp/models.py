from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Diseases(models.Model):
    name=models.CharField(max_length=1000,blank=False)
    about=models.CharField(max_length=1000,blank=False)
    symptoms=models.CharField(max_length=1000,blank=False)
    treatment=models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return self.name

