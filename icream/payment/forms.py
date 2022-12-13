from django import forms
from . import models



class AddAddress(forms.ModelForm):
    class Meta:
        model = models.OrderAddress
        fields = ('username','phone_number','email','address','state','pincode','city')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control p-4',}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control p-4',}),
            'email':forms.EmailInput(attrs={'class':'form-control p-4',}),
            'address' : forms.Textarea(attrs={'class':'form-control p-4',}),
            'state' : forms.TextInput(attrs={'class':'form-control p-4',}),
            'pincode' : forms.NumberInput(attrs={'class':'form-control p-4',}),
            'city' : forms.TextInput(attrs={'class':'form-control p-4',}),
        }
        labels = {
            'username':'User Name',
            'phone_number': 'Phone Number' ,
            'email': 'Email' ,
            'address' : 'Address' ,
            'state' : 'State' ,
            'pincode' : 'Pincode' ,
            'city' : 'City' ,
        }




class AddCoupons(forms.ModelForm):
    pass