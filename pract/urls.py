from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('register_patients',views.register_patients,name="register_patient"),
    path('register_doctors',views.register_doctors,name="register_doctor"),
    path('logincheckDoctor',views.logincheckDoctor,name='logincheckDoctor'),
    path('logincheckPatient',views.logincheckPatient,name='logincheckPatient'),
    path('loginDoctor',views.loginDoctor,name='loginDoctor'),
    path('loginPatient',views.loginPatient,name='loginPatient'),
    path('openPatProfCheck',views.openPatProfCheck,name="openPatProfCheck"),
    path('addReport',views.addReport,name="addReport"),
    path('addingReport',views.addingReport,name="addingReport")
]