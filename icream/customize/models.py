from django.db import models
from home.models import Category


# Create your models here.


class Banner(models.Model):

    banner_name = models.CharField(max_length=30,default=None)
    banner_image = models.ImageField(upload_to='banner/',default=None)

    def __str__(self):
        return self.banner_name

        

class Coupon(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,default=None)
    coupon_name = models.CharField(max_length=20,null=True,default=None)
    offers = models.IntegerField(null=True,default=None)

