from django import forms
from django.contrib.auth.models import User

class AddProductForm(forms.Form):
     product_name = forms.CharField(label='Product Name', max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Product Name'}))
     company_name = forms.CharField(label='Product Company Name', max_length=100,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter company name'}))
     product_image = forms.ImageField(label='Product Image')
     product_price = forms.DecimalField(label='Product Price',required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter price ','min':'0'}))
     entered_by = forms.ModelChoiceField(label='Entered By', queryset=User.objects.all())

