from . import views
from django.urls import path

app_name = 'patient'
urlpatterns = [
    path('login/',views.login,name ='login'),
    path('register/',views.register,name ='register')
]
