from django.db import models
from home.models import Orders,UserInfo
from datetime import datetime

now = datetime.now()

# Create your models here.



class OrderAddField(Orders):
    order_time = models.TimeField(default=now)
    product_qty = models.IntegerField(default=None)
    product_total = models.IntegerField(default=None)

     



class OrderAddress(models.Model):
    '''
    user address 
    '''
    username = models.CharField(max_length=20)
    phone_number = models.BigIntegerField(default=None)
    email = models.EmailField(default=None, max_length=254)
    address = models.TextField(default=None)
    state = models.CharField(default=None,max_length=30)
    pincode = models.IntegerField(default=None)
    city = models.CharField(max_length=30,default=None)
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE,default=None,blank=True,null=True)




class OrderCoupon(models.Model):
    '''
    
    '''
    c_off = models.IntegerField( default=None )
    c_name = models.CharField(max_length=30,default=None)
    c_description = models.TextField(default=None)
    is_use = models.BooleanField(default=None)

    def __str__(self):
        return self.c_name



class OrderPackage(models.Model):
    '''
    orderPackage class is handle any coupon apply is user 
    and manage orders 
    devide each orders
    '''
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=None)
    is_coupon_apply = models.ForeignKey(OrderCoupon, on_delete=models.CASCADE,default=None,blank=True,null=True)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE,default=None,blank=True)






class OrderList(models.Model):
    '''
    
    '''
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to='orders/', default=None)
    product_price = models.IntegerField(default=None)
    product_discription = models.TextField(default=None)
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(default=now)
    product_qty = models.IntegerField(default=None)
    product_total = models.IntegerField(default=None)
    is_cancel = models.BooleanField(default=None)
    is_delivered = models.BooleanField(default=None)
    payment_type = models.CharField(max_length=10)
    address = models.ForeignKey(OrderAddress, on_delete=models.CASCADE,default=None)
    is_payment = models.BooleanField(default=None)
    order_pack = models.ForeignKey(OrderPackage, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.product_name
