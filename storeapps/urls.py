from django.urls import path
from .views import  *

urlpatterns = [  
     path("", index,name='home'),
     path("courseform", courseForm,name='courseform'),
     path("course/<int:id>", cousre_Detail,name='courseDetailsurs'),
]