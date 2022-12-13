from home.models import UserInfo
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