from . import views
from django.urls import path

app_name = 'patient'
urlpatterns = [

    path('patientProfile/', views.patientProfile, name='patientProfile'),
    path('patientRecords/', views.patientRecords, name='patientRecords'),
    path('personalNotes/', views.personalNotes, name='personalNotes'),

    # path('login/',views.login,name ='login'),
    path('registerpage/',views.registerpage,name ='registerpage'),
    path('profile/',views.profile,name ='profile'),
    path('patientregister/',views.patientregister,name = 'patientregister'),
    path('makeprofilepage/',views.makeprofilepage,name = 'makeprofilepage'),
    path('signup/',views.signup, name ='signup'),
    path('loginp/',views.loginn, name ='loginp'),
    path('logout/',views.logout, name ='logout'),

]
