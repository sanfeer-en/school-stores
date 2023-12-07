from django.urls import path
from .views import  *

urlpatterns = [  
     path("", index,name='home'),
     
     path("course", cousre_Detail,name='courseDetailsurs'),
     path("orderform", orderForm,name='orderForm'),
     path('get_courses/<int:department_id>/', get_courses, name='get_courses'),



     # path("courseform", courseForm,name='courseform'),
     path('oderconfirm', order_Confirmed,name='order_Confirmed'),
]