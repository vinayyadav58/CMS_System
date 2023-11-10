from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'})#for applying CSS
    )
    password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Password','type':'password'})
    )

    password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm Password','type':'password'})
    )
   

class details_emp_form(forms.Form):
            first_name = forms.CharField(label='First Name',required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
            last_name = forms.CharField(label='last Name',required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
            email = forms.EmailField(label='Email ',required=True,max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}))
            Joining_date = forms.DateField(label='Date of joining',required=True,widget = forms.DateInput(attrs={'type': 'date','class':'form-control','placeholder':'select date '}))
            activtiy = forms.ChoiceField(
                   label='Select status',
                   choices=[
                          ('Choose', 'Choose'),
                          ('Active', 'Active'),('Inactive', 'Inactive')
                   ],required=True
            )


    