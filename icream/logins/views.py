from django.shortcuts import render,redirect
from .forms import Login,Registration,LoginWithOtp
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.cache import cache_control
from .models import UserInfo

from . import helper



# login start

@cache_control(no_cache = True,must_revaliddate = True,no_store = True)
def login(request):
    '''
    this is the login function admin login and user login same function
    values validate and authenticated to database then create session
    admin session and user session is superated
    '''
    forms = Login(request.POST or None)
    if 'username' in request.session:
        return redirect('guest_user_home')

    if request.method == 'POST':

        if forms.is_valid():
            login_username = request.POST['username']
            login_password = request.POST['password']
            try:
                user = authenticate(request,username=login_username,password= login_password)
            except:
                messages.error(request,'Your Not Valid')
                return redirect('login')
            else:
                if user is not None :

                    if user.is_superuser:
                        request.session['adminusername'] = login_username
                        print(request.session['adminusername'])
                        print(type(request.session['adminusername']))
                        return redirect('dashbord')
                    
                    if not UserInfo.objects.get(username=login_username).is_block:
                        request.session['username'] = login_username
                        helper.username = login_username
                        return redirect('guest_user_home')
                    
                    messages.error(request,'Your account has been blocked')
                    return redirect('login')
                messages.error(request,'user is not valid')

    return render(request,'login.html',{'formfield':forms})


# login end

# registration start

# registration

@cache_control(no_cache = True,must_revaliddate = True,no_store = True)
def registration(request):
    '''
    registratioin function "password is session handile varible 
    validate password and confirm password and authenticate values in database 
    then chek user name and phone number is unique then create user
    "'''

    forms = Registration(request.POST or None)
    if 'password' in request.session:
        return redirect('guest_user_home')

    if request.method == 'POST':

        username = request.POST['username']
        phone_number = request.POST['phone_number'] 
        register_password = request.POST['password']
        register_confirm_password = request.POST['passwordconfirm']

        if register_confirm_password == register_password:
            if forms.is_valid():
                user_confirm = authenticate(username=username,password=register_confirm_password)
                if user_confirm is None:
                    try:
                        UserInfo.objects.get(username = username)
                    except UserInfo.DoesNotExist :
                        phone_number_taken_check = UserInfo.objects.all()
                        for item in phone_number_taken_check:
                            if item.phone_number == int(phone_number):

                                messages.error(request,'phone number already taken')
                                return redirect('registration')
                        

                        helper.username = username
                        helper.phone = phone_number
                        otp_number = helper.otp()
                        request.session['otpnumber'] = otp_number()
                        request.session['registerusernam'] = username
                        request.session['registerphone'] = phone_number
                        request.session['registerpassword'] = register_confirm_password
                        helper.password = register_confirm_password
                        helper.otp_number = otp_number

                        return redirect('otp_vlidate')

                    else:
                            
                        messages.error(request,'user is already exist')
                        return redirect('registration')

                messages.error(request,'user is already exist')
                return redirect('registration')
                
        else:
            messages.error(request,'password not same')

    return render(request,'registration.html',{'formfield':forms})



#otp validation

def otp_validate(request):
    
    if request.method == 'POST':
        user_input_otp = int(request.POST['otp_number'])
        # print(f"otp user input {user_input_otp} and type of it {type(user_input_otp)}")
        # print(f"otp number in session {request.session['otpnumber']} and type {type(request.session['otpnumber'])}")
        # print(f"if condition check for why its not working {int(user_input_otp) == (request.session['otpnumber'])}")
        if int(user_input_otp) == int(request.session['otpnumber']):
            user = UserInfo()
            user.username = request.session['registerusernam']
            user.password = request.session['registerpassword']
            user.phone_number = request.session['registerphone']
            user.is_block = False
            # user = UserInfo.objects.create_user(username=helper.username,password=helper.password,phone_number = helper.phone,is_block=0)
            user.save()
            request.session.flush()
            request.session['username'] = user.username
            return redirect('guest_user_home')
        
        messages.error(request,'otp is not currect')
        
    return render(request,'otpgenerate.html')



# registration end 

# Login with otp start

# varifyotp

def verifyotp(request):
    forms = LoginWithOtp(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            # global access variable


            # get values in forms

            username = request.POST['username']
            phone_number = request.POST['phone_number']

            helper.phone =phone_number
            # exection 

            try:
                user_is_valid_or_not = UserInfo.objects.get(username = username)
            except UserInfo.DoesNotExist:
                messages.error(request,'user is not valid')
                return redirect('verifyotp')
            else:
                if user_is_valid_or_not.phone_number == int(phone_number):

                    if not UserInfo.objects.get(username=username).is_block:

                        
                        otp_number = helper.otp()
                        request.session['otpnumber'] = otp_number()
                        helper.otp_number = otp_number
                        helper.username = username
                        

                        return redirect('phone_with_otp')

                    messages.error(request,'Your account is blocked')
                    return redirect('login')

                messages.error(request,'phone number is not valid')
    return render(request,'phonenumber.html',{'formfield':forms})



# login with otp and phone number

def phone_with_otp(request):
    if request.method == 'POST':
        user_input_otp = int(request.POST['otp_number'])
        
        if int(user_input_otp) == int(request.session['otpnumber']):
            user = UserInfo.objects.get(username = helper.username)
            request.session['username'] = helper.username
            del request.session['otpnumber']
            return redirect('guest_user_home')

        messages.error(request,'otp is not currect')
    return render(request,'otpgenerate.html')

#Login with otp end

# forget password start

# forget password

def forget_password(request):
    forms = LoginWithOtp(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():

            username = request.POST['username']
            phone_number = request.POST['phone_number']
            try:
                user_is_valid_or_not = UserInfo.objects.get(username = username)
            except UserInfo.DoesNotExist:
                messages.error(request,'user is not valid')
                return redirect('forget_password')
            else:
                if user_is_valid_or_not.phone_number == int(phone_number):
                    otp_number = helper.otp()
                    helper.otp_number = otp_number
                    return redirect('user_confirm')
                messages.error(request,'phone number is not valid')
    return render(request,'forgetpassword.html',{'formfield':forms})


# userconfirm

def user_confirm(request):
    if request.method == 'POST':
        user_input_otp = request.POST['otp_number']
        if int(user_input_otp) == helper.otp_number():

            return redirect('re_password')
            
        messages.error(request,'otp is not currect')
    return render(request,'userconfirm.html')



# repassword

def re_password(request):
    return render(request,'repassword.html')



# forget password end



# Logouts

# user logout

def user_logout(request):
    request.session.flush()
    return redirect('guest_user_home')



# admin logout

def admin_logout(request):
    request.session.flush()
    return redirect('guest_user_home')
    
