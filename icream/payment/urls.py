from django.urls import path
from . import views

urlpatterns = [
    path('razopay<total>/',views.payment_with_razopay,name='payment_with_razopay'),
    path('userplaceorder/',views.user_place_order,name='user_place_order'),
    path('addaddress/',views.add_address,name='add_address'),
    path('cashondelivery/<int:id>/<ptype>',views.cash_on_delivery,name='cash_on_delivery'),

]
