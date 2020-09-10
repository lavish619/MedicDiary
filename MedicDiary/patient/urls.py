from . import views
from django.urls import path

app_name = 'patient'
urlpatterns = [
    # path('login/',views.login,name ='login'),
    path('registerpage/',views.registerpage,name ='registerpage'),
    path('signup/',views.signup, name ='signup'),
    path('loginp/',views.loginn, name ='loginp'),
    path('logout/',views.logout, name ='logout'),

]
