from django.urls import path
from . import views


urlpatterns = [
    path('',views.guest_user_home,name='guest_user_home'),
    path('about/',views.about,name='about'),
    path('profile/',views.user_profile,name='user_profile'),
    path('ordertrack/',views.user_order_track,name='user_order_track'),
    path('ordertrack/cancel',views.cancel_order,name='cancel_order'),
    path('addcoupon/',views.addcoupon,name='addcoupon'),
    path('orderproducts/<id>',views.orders_all_product,name="orders_all_product"),
    path('userdetailsedit/<id>',views.edituser_details,name='edituser_details'),
    

]
