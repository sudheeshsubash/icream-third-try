from django.shortcuts import render,redirect
from logins.models import UserInfo
from home.models import Product,Category
from .models import Banner
from .forms import ProductEditDetails,ProductAddDetails,AddCategory,AddBanner
import os
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.


# product table start 

def product_table(request):
    '''
        show product details
    '''

    # pagination 
    p = Paginator(Product.objects.all(),5)
    page = request.GET.get('page')
    product_details = p.get_page(page)

    return render(request,'producttable.html',{'product_details':product_details})



def delete_product(request):
    id = request.GET['productid']
    delete_product = Product.objects.get(id = id)

    delete_product.delete()
    return JsonResponse({'value':True})




def edit_product(request,id):
    '''
    this is the edit product fuction
    '''
    edit_product_details = Product.objects.get(id = id)
    forms = ProductEditDetails(request.POST or None,instance= edit_product_details )
    if request.method == 'POST':
    
        # here try except is user check the image field 
        
        try:

            product_image = request.FILES['product_image']

        except :

            forms.save()
            return redirect('product_table')

        else:
            forms.save()

            edit_product_details.product_image = product_image
            edit_product_details.save()
            return redirect('product_table')

    return render(request,'editproduct.html',{'forms':forms})



def add_product(request):
    """
    Add Products
    """
    forms = ProductAddDetails(request.POST or None)
    product_add = Product()

    if request.method == 'POST':
        print(request.FILES)
        product_name = request.POST['product_name']
        product_image = request.FILES['file']
        product_price = request.POST['product_price']
        product_discription = request.POST['product_discription']
        category_id = request.POST['Cutegory_id']
        
        product_add.product_name = product_name
        product_add.product_price = product_price
        product_add.product_image = product_image
        product_add.product_discription = product_discription
        product_add.Cutegory_id_id = category_id
        product_add.is_available = 100

        product_add.save()

        return JsonResponse({'output':True})

    return render(request,'addproduct.html',{'forms':forms})



# product table end


# user table customize functions start

def user_table(request):
    """
    this is user details list fuctions 
    """

    # pagination 
    p = Paginator(UserInfo.objects.all(),5)
    page = request.GET.get('page')
    user_details = p.get_page(page)

    return render(request,'usertable.html',{'user_details':user_details})
    


def user_block(request):
    '''
        this function user block users
    '''
    id = request.GET['productid']
    block_user_details = UserInfo.objects.get(id = id)
    block_user_details.is_block = 1
    block_user_details.save()
    return JsonResponse({'value':True})



def user_unblock(request,id):
    '''
        this function user unblock the user
    '''

    block_user_details = UserInfo.objects.get(id = id)
    block_user_details.is_block = 0
    block_user_details.save()
    return redirect('user_table')


# user details fucntion end


# category start

def product_category(request):
    category_name = Category.objects.all()
    return render(request,'category.html',{'category_name':category_name})



def add_product_category(request):
    forms = AddCategory(request.POST or None)
    if request.method == 'POST':

        forms.save()
        
        return redirect('product_category')
    return render(request,'addcategory.html',{'forms':forms})


# category end 


# banner start 


def banners(request):
    banner_details = Banner.objects.all()
    return render(request,'banner.html',{'banner_details':banner_details})




def add_banner(request):
    
    forms = AddBanner(request.POST or None )
    if request.method == 'POST':
        if forms.is_valid():

            print(forms)
            forms.save()

            return redirect('banners')
    return render(request,'addbanner.html',{'forms':forms})


# banner end
