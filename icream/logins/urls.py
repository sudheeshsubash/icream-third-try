from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
    path('logout/',views.user_logout,name='logout'),
    path('otpgenerate/',views.otp_validate,name='otp_vlidate'),
    path('phonenumberwithotp/',views.phone_with_otp,name='phone_with_otp'),
    path('adminlogout/',views.admin_logout,name='admin_logout'),
    path('repassword/',views.re_password,name='re_password'),
    path('forgetpassword',views.forget_password,name='forget_password'),
    path('userconfirm/',views.user_confirm,name='user_confirm'),

]
 