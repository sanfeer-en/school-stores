from django.urls import path
from .views import  *

# from django.urls import path
# from . import  views 

urlpatterns = [

    path('register',register,name ='register'),
    path('login',login,name ='login'),
    path('logout',logout,name ='logout'),
]