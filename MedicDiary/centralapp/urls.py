from . import views
from django.urls import path

app_name = 'centralapp'
urlpatterns = [

    path('',views.mainpage,name='mainpage'),
    path('about_us/',views.about_us,name ='about_us')
]
