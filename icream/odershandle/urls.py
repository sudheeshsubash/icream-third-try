from django.urls import path
from . import views


urlpatterns = [
    path('',views.dashbord,name='dashbord'),
    path('history',views.order_history,name='order_history'),
    path('couponview/',views.coupon_view,name='coupon_view'),
    path('addcoupon/',views.add_coupons,name='add_coupons'),
    path('cancle/',views.cancle_coupon,name='cnacle_coupon'),
    path('coupon/',views.coupons,name='coupoons')
    
]
