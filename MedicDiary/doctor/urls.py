from . import views
from django.urls import path

app_name = 'doctor'
urlpatterns = [
      path('registerpage/',views.registerpage,name ='registerpage'),
       path('signup/',views.signup, name ='signup'),
         path('logind/',views.loginn, name ='logind'),
          path('myPatients/', views.myPatients, name='myPatients'),
          path('doctorProfile/', views.doctorProfile, name='doctorProfile'),
          path('addpatient/', views.addpatient, name='addpatient'),
          path('doctorRecords/<str:p_username>', views.doctorRecords, name='doctorRecords'),
           path('addRecord/', views.addRecord, name='addRecord'),
            path('newReport/', views.newReport, name='newReport'),


    # path('doclogin/',views.doclogin,name ='doclogin'),
    # path('docregister/',views.docregister,name ='docregister')
]
