from django import forms
from .models import Doctor,Appointment,Deal
from products.models import Product
from django.contrib.auth.models import User


class AddDoctorForm(forms.Form):
    # class Meta:
    #     model = Doctor
        # fields = ['doctor_name', 'specialisation', 'contact_number', 'location']
        doctor_name = forms.CharField(label='Doctor Name',required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Doctor Name'}))
        specialisation = forms.ChoiceField(
            label='Doctor Specialisation',
            choices=[('Choose', 'Choose'),('Chest', 'Chest'),
                     ('Heart', 'Heart'),
                     ('General', 'General'),('Orthopaedic', 'Orthopaedic')],
                     required=True,)
        contact_number = forms.IntegerField(label='Doctor Contact Number',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter  Number','min':'0','pattern':"[1-9]{1}[0-9]{9}"}))
        location = forms.CharField(label='Doctor Location',required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Location'}))
        entered_by = forms.ModelChoiceField(label='Entered By', queryset=User.objects.all())




class ScheduleAppointmentForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label='Doctor')
    date = forms.DateField(label='Date of Schedule',required=True,widget = forms.DateInput(attrs={'type': 'date','class':'form-control','placeholder':'select date ','min':"{new Date().toISOString().split('T')[0]} /"}))
    time = forms.TimeField(label='Time of Schedule',required=True,widget = forms.TimeInput(attrs={'type': 'time' ,'class':'form-control','placeholder':'select  time '}))
    entered_by = forms.ModelChoiceField(label='Entered By', queryset=User.objects.all())



class DealForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label='Doctor')
    product_name = forms.ModelChoiceField(required=True,queryset=Product.objects.all(), label='Product')
    # product_name = forms.CharField(label='Product Name',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter product name'}))
    quantity_ordered = forms.IntegerField(label='Quantity Ordered',required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter quantity ordered','min':'0'}))
    entered_by = forms.ModelChoiceField(label='Entered By', queryset=User.objects.all())


class DoctorVisitsForm(forms.Form):
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())
    month = forms.ChoiceField(choices=[(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')]) 

class visitDoctorVisitsForm(forms.Form):
    # doctor_name = forms.ModelChoiceField(queryset=Doctor.objects.all())
    employee_name = forms.ModelChoiceField(queryset=User.objects.all())
    month = forms.ChoiceField(choices=[(1, 'January'), (2, 'February'), (3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')])  
