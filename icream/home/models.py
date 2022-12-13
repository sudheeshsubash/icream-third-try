from django.db import models
from logins.models import UserInfo



# product models start 

class Category(models.Model):
    '''
    product category 
    '''
    category_name = models.CharField(max_length=30,default=None)
    
    def __str__(self):
        return self.category_name



class Product(models.Model):
    '''
    Products
    '''
    product_name = models.CharField(max_length=50,default=None)
    product_price = models.IntegerField(default=None)
    product_image = models.ImageField(upload_to='images/',default=None)
    product_discription = models.TextField(default=None)
    Cutegory_id = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    is_available = models.IntegerField(default=None)
    is_offers = models.IntegerField(default=None)


    def __str__(self):
        return self.product_name


class ProductWishlist(models.Model):
    '''
    
    '''
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE,default=None)
    product_id = models.ForeignKey(Product,  on_delete=models.CASCADE,default=None)

 

class ProductCart(models.Model):
    '''
    
    '''
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE,default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,default=None)
    cart_quantity = models.IntegerField(default=None)
    total_price = models.IntegerField(default=None)
    
    


class ProductReview(models.Model):
    '''
    
    '''
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE,default=None)
    message = models.TextField(default=None)
    rate = models.IntegerField(default=None)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE,default=None)
    




class Orders(models.Model):
    '''
    
    '''
    username = models.CharField(max_length=20,default=None)
    product_name = models.CharField(max_length=50,default=None)
    product_image = models.ImageField(upload_to='orders/',default=None)
    product_price = models.IntegerField(default=None)
    product_discription = models.TextField(default=None)
    order_date = models.DateField(auto_now_add=True)
    order_type = models.CharField(max_length=20,default=None)
    user_address = models.TextField(default=None)
    user_phone = models.BigIntegerField(default=None)
    user_state = models.CharField(max_length=30,default=None)
    user_pincode = models.IntegerField(default=None)
    user_email = models.EmailField( max_length=254,default=None)



