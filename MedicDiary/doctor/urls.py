from . import views
from django.urls import path

app_name = 'doctor'
urlpatterns = [
    path('doctorprofile/', views.doctor_profile, name='doctor_profile'),
    path('myPatients/', views.myPatients, name='myPatients'),
    path('doctorRecords/', views.doctorRecords, name='doctorRecords'),
    path('registerpage/',views.registerpage,name ='registerpage'),
    path('signup/',views.signup, name ='signup'),
    path('logind/',views.loginn, name ='logind'),
    # path('doclogin/',views.doclogin,name ='doclogin'),
    # path('docregister/',views.docregister,name ='docregister')
]
