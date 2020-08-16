from . import views
from django.urls import path

app_name = 'doctor'
urlpatterns = [
    path('doclogin/',views.doclogin,name ='doclogin'),
    path('docregister/',views.docregister,name ='docregister')
]
