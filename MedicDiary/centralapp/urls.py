from . import views
from django.urls import path

app_name = 'centralapp'
urlpatterns = [

    path('',views.mainpage,name='mainpage'),
    path('About_us/',views.About_us,name ='About_us'),
    path('Aids/',views.Aids,name ='Aids'),
    path('Cancer/',views.Cancer,name ='Cancer'),
    path('Covid-19/',views.Covid_19,name ='Covid_19'),
    path('Diabetes/',views.Diabetes,name ='Diabetes'),
    path('FAQS/',views.FAQS,name ='FAQS'),
    path('Heart_disorder/',views.Heart_disorder,name ='Heart_disorder'),
    path('medical_practitioners/How_to_use',views.doc_how_to_use,name ='doc_how_to_use'),
    path('friends-and-family/How_to_use',views.patients_how_to_use,name ='patients_how_to_use'),
    path('Hypertension/',views.Hypertension,name ='Hypertension'),
    path('Inside_health_records/',views.Inside_health_records,name ='Inside_health_records'),    ]
