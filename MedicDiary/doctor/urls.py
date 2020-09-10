from . import views
from django.urls import path

app_name = 'doctor'
urlpatterns = [
      path('registerpage/',views.registerpage,name ='registerpage'),
       path('signup/',views.signup, name ='signup'),
         path('logind/',views.loginn, name ='logind'),
    # path('doclogin/',views.doclogin,name ='doclogin'),
    # path('docregister/',views.docregister,name ='docregister')
]
