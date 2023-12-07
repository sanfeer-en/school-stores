from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'dob',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'age',
            }),
            'gender': forms.RadioSelect(attrs={
                'class': 'form-radio',
                'id': 'gender',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone_number',
            }),
            'mail_id': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'mail',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'address',
            }),
            'department': forms.Select(attrs={
                'class': 'custom-select',
                'id': 'depart',
            }),
            'course': forms.Select(attrs={
                'class': 'custom-select',
                'id': 'course',
            }),
            'purpose': forms.Select(attrs={
                'class': 'custom-select',
                'id': 'purpose',
            }),
            'materials_provide': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-checkbox',
                'id': 'material_provide',
            }),
        }