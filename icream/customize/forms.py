from django.forms import ModelForm
from django import forms
from home.models import Product,Category
from .models import Banner,Coupon


class ProductEditDetails(ModelForm):
    '''
    Product details edit form
    '''
    # product_image = forms.ImageField(label=('product_image'),required=False, error_messages={'invalid':('image field only')},widget=forms.FileInput(attrs={'name':'img'}))
    class Meta:
        model = Product
        fields = ('product_name','product_price','product_image','product_discription','Cutegory_id','is_available')
        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_price':forms.NumberInput(attrs={'class':'form-control'}),
            'product_image':forms.FileInput(attrs={'class':'form-control'}),
            'product_discription':forms.Textarea(attrs={'class':'form-control'}),
            'is_available':forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }
        labels={
            'product_name':'Product Name',
            'product_price':'Product Price',
            'product_image':'Product Image',
            'product_discription':'Product Discription',
            'Cutegory_id':'Cutegory Id',
        }




class ProductAddDetails(ModelForm):
    '''
    product value get or set form
    '''

    product_image = forms.ImageField(label=('product_image'),required=False, error_messages={'invalid':('image field only')},widget=forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        model = Product
        fields = ('product_name','product_price','product_image','product_discription','Cutegory_id')
        widgets = {
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_price':forms.NumberInput(attrs={'class':'form-control'}),
            'product_discription':forms.Textarea(attrs={'class':'form-control'}),
            
            
        }
        labels={
            'product_name':'Product Name',
            'product_price':'Product Price',
            'product_image':'Product Image',
            'product_discription':'Product Discription',
            'Cutegory_id':'Category Id',
        }




class AddCategory(ModelForm):
    '''
    this is caregory add form
    '''
    class Meta:
        model = Category
        fields = ('category_name',)
        widgets = {
            'category_name':forms.TextInput(attrs={'class':'form-control'})
        }



class AddBanner(ModelForm):
    '''
    add new banner value get form
    '''

    banner_image = forms.ImageField(label=('banner_image'),required=False, error_messages={'invalid':('image field only')},widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Banner
        fields = ('banner_name','banner_image')
        widgets = {
            'banner_name':forms.TextInput(attrs={'class':'form-control'}),
            'banner_image':forms.FileInput(attrs={'class': 'form-control'}),

        }
        



class AddCoupon(ModelForm):
    class Meta:
        model = Coupon
        fields = ('category','coupon_name','offers')
        widgets = {
            'coupon_name':forms.TextInput(attrs={'class':'form-control'}),
            'offers':forms.NumberInput(attrs={'class':'form-control'}),
        }
 