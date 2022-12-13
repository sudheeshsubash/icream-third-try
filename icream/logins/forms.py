from .models import UserInfo
from django.forms import ModelForm
from django import forms
import re


class Login(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username','password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','maxlength':"20"}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),

        }
        labels={
            'username':'User Name',
            'password':'Password',

        }
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not re.match("^[A-Za-z]{3,12}$",username):
            raise forms.ValidationError("username only alow alphabets ")

        if len(password) < 4 or len(password)> 12:
            raise forms.ValidationError("password length beetween 4 - 12 ")



class Registration(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username','phone_number','password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),


        }
        labels={
            'username':'User Name',
            'phone_number':'Phone Number',
            'password':'Password',

        }
    def clean(self):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            phone_number = self.cleaned_data['phone_number']


            if not re.match("^[A-Za-z]{3,12}$",username):
                raise forms.ValidationError("username only alow alphabets ")

            if len(password) < 4 or len(password)> 12:
                raise forms.ValidationError("password length beetween 4 - 12 ")
            
            if not len(str(phone_number)) == 10:
                raise forms.ValidationError("phone number is not valid")



class LoginWithOtp(ModelForm):
    class Meta:
        model = UserInfo
        fields = ('username','phone_number')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),


        }
        labels={
            'username':'User Name',
            'phone_number':'Phone Number',

        }
    def clean(self):
            username = self.cleaned_data['username']
            phone_number = self.cleaned_data['phone_number']


            if not re.match("^[A-Za-z]{3,12}$",username):
                raise forms.ValidationError("username only alow alphabets ")
            
            if not len(str(phone_number)) == 10:
                raise forms.ValidationError("phone number is not valid")


