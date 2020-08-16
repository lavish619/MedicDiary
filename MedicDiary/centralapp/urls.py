from . import views
from django.urls import path

app_name = 'centralapp'
urlpatterns = [

    path('',views.mainpage,name='mainpage'),
]
