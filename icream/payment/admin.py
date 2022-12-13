from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(OrderAddField)
admin.site.register(OrderAddress)
admin.site.register(OrderList)
admin.site.register(OrderCoupon)
admin.site.register(OrderPackage)