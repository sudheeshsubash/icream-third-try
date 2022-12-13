from django import forms
from .models import Orders


class UserOrderPlace(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('user_email','user_state','user_pincode','user_phone','user_address')
        widgets = {
            'user_email':forms.EmailInput(attrs={'class':'form-control p-4',}),
            'user_state':forms.TextInput(attrs={'class':'form-control p-4',}),
            'user_pincode':forms.TextInput(attrs={'class':'form-control p-4',}),
            'user_phone' : forms.TextInput(attrs={'class':'form-control p-4',}),
            'user_address' : forms.Textarea(attrs={'class':'form-control p-4',}),
        }
        labels = {
            'user_email':'Email',
            'user_state':'State',
            'user_pincode':'Pincode',
            'user_phone':'Phone',
            'user_address':'Address',
        }