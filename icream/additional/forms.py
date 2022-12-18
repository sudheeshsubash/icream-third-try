from home.models import UserInfo
from payment.models import OrderAddress
from django import forms



class EditUserDetails(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username','first_name','last_name','email','phone_number')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }
        labels={
            'username':"User Name",
            'first_name':"First Name",
            'last_name':"Last Name",
            'email':"Email",
            'phone_number':"Phone Number",
        }



class EditUserAddress(forms.ModelForm):
    class Meta:
        model = OrderAddress
        fields = ('username','phone_number','email','address','state','pincode','city',)
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }
        labels={
            'username':"User Name",
            'phone_number':"Phone NUmber",
            'email':"Email",
            'address':"Address",
            'state':"State",
            'pincode':"Pincode",
            'city':"City",
        }
        