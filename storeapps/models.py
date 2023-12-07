from django.db import models
from django.contrib.auth.models import User
from django import forms

# User Profile model (moved to the top)

  
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_PURPOSE_CHOICES = [
        ('place_order', 'Place Order'),
        ('return', 'Return'),
        ('enquiry', 'Enquiry'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]


    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='male')
    phone_number = models.CharField(max_length=10)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default='Select department')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50, choices=ORDER_PURPOSE_CHOICES)
    materials_provide = models.ManyToManyField(Material)

    def __str__(self):
        return self.name


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose', 'materials_provide']

#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args, **kwargs)
#         self.fields['course'].queryset = Course.objects.none()