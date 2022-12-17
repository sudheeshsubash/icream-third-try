from django.shortcuts import render,redirect
from .models import *
from logins import helper
from home.models import UserInfo
from .forms import UserOrderPlace
from customize.models import Banner,Coupon
from django.core.paginator import Paginator
from django.http import JsonResponse
from odershandle.views import check_order_offers
import json
# Create your views here.


# product

def product(request):
    '''
    
    '''
    # Check offers before display product details
    check_order_offers()
    # edit offer price in product table 

    # pagination

    p = Paginator(Product.objects.all(),4)
    page = request.GET.get('page')
    product_pagination = p.get_page(page)
    coupon = Coupon.objects.all()
    category_list = Category.objects.all()
    '''
    this for loop change price offer apply
    '''
    if request.method == 'POST':
        categoryname = request.POST['categoryname']
        print(categoryname)
        p = Paginator(Product.objects.filter(Cutegory_id = categoryname),4)
        page = request.GET.get('page')
        product_pagination = p.get_page(page)

    if 'username' in request.session:
        user_id = UserInfo.objects.get(username = request.session['username'])
        cart_badge = len(ProductCart.objects.filter(user_id_id = user_id.id))
        wishlist_badge = len(ProductWishlist.objects.filter(user_id_id = user_id.id))
        return render(request,'product.html',{'coupon':coupon,'category_list':category_list,'product_pagination':product_pagination,'cart_badge':cart_badge,'wishlist_badge':wishlist_badge})

    return render(request,'product.html',{'coupon':coupon,'category_list':category_list,'product_pagination':product_pagination})



def category_product(request,id):
    return JsonResponse({'data':id})

# details

def details(request,id):
    product_details = Product.objects.get(id = id)
    product_review = ProductReview.objects.filter(product_id_id = id)
    rate = 'aaaaa'
    if 'username' in request.session:
        user_id = UserInfo.objects.get(username = request.session['username'])
        cart_badge = len(ProductCart.objects.filter(user_id_id = user_id.id))
        wishlist_badge = len(ProductWishlist.objects.filter(user_id_id = user_id.id))
        return render(request,'details.html',{'product_details':product_details,'product_review':product_review,'rate':rate,'cart_badge':cart_badge,'wishlist_badge':wishlist_badge,})

    return render(request,'details.html',{'product_details':product_details,'product_review':product_review,'rate':rate,})



# cart  start 

def cart(request):

    user_id = UserInfo.objects.get(username = request.session['username'])
    cart_list = ProductCart.objects.filter(user_id_id = user_id.id ).select_related('product_id')
    wishlist_badge = len(ProductWishlist.objects.filter(user_id_id = user_id.id))

    total = int()
    for x in cart_list:
        total += x.total_price
    helper.total = total
    helper.couponid = 0
    print(helper.total)
    return render(request,'cart.html',{'cart_list':cart_list,'total':total,'wishlist_badge':wishlist_badge,})



def add_to_cart(request):
    '''
    add to cart 
    '''
    user_id = UserInfo.objects.get(username = request.session['username'])
    id = request.GET['pid']
    
    if ProductCart.objects.filter(product_id_id = id).exists():
        return JsonResponse({'value':1})
    else:
        product_cart = ProductCart()
        product_cart.user_id_id = user_id.id
        product_cart.product_id_id = id
        product_cart.cart_quantity = 1
        product_cart.total_price = product_cart.product_id.is_offers

        product_cart.save()
        total_products_in_cart = len(ProductCart.objects.filter(user_id_id = user_id.pk))
        print(total_products_in_cart)
        return JsonResponse({'value':0,'cartquantity':total_products_in_cart})




def increase_quantity_cart(request):
    '''
    
    '''
    user_id = UserInfo.objects.get(username = request.session['username'])
    id = request.GET['id']
    cart_details = ProductCart.objects.filter(user_id_id = user_id.id).get(product_id_id = id)
    cart_details.cart_quantity += 1
    cart_details.total_price = cart_details.product_id.is_offers * cart_details.cart_quantity
    cart_details.save()
    '''
    after save fetch all user cart data
    '''
    cart_list = ProductCart.objects.filter(user_id_id = user_id.id ).select_related('product_id')
    total = int()
    for x in cart_list:
        total += x.total_price
    helper.total = total
    return JsonResponse({'quantity':cart_details.cart_quantity,'total':total})




def decrese_quantity_cart(request):
    '''
    
    '''
    user_id = UserInfo.objects.get(username = request.session['username'])
    id = request.GET['id']
    cart_details = ProductCart.objects.filter(user_id_id=user_id.id).get(product_id_id = id)
    cart_details.cart_quantity -= 1
    if cart_details.cart_quantity == 0:
        cart_details = ProductCart.objects.filter(user_id_id=user_id.id).get(product_id_id = id).delete()
        return JsonResponse({'quantity':0})
    cart_details.total_price = cart_details.cart_quantity * cart_details.product_id.is_offers
    cart_details.save()
    '''
    after save fetch all user cart data
    '''
    cart_list = ProductCart.objects.filter(user_id_id = user_id.id ).select_related('product_id')
    total = int()
    for x in cart_list:
        total += x.total_price
    helper.total=total
    return JsonResponse({'quantity':cart_details.cart_quantity,'total':total})
    



def remove_cart(request):
    '''
    remove from cart
    '''
    user_id = UserInfo.objects.get(username = request.session['username'])
    pid = request.GET['productid']
    ProductCart.objects.filter(user_id_id=user_id.id).filter(product_id_id = pid).delete()
    return JsonResponse({'result':'deleted'})

# cart end



# wishlist

def product_wishlist(request):
    '''
    product wishlist show
    '''
    user_id = UserInfo.objects.get(username = request.session['username'])
    product_list = ProductWishlist.objects.filter(user_id_id = user_id.id ).select_related('product_id')
    cart_badge = len(ProductCart.objects.filter(user_id_id = user_id.id))

    return render(request,'wishlist.html',{'product_list':product_list,'cart_badge':cart_badge,})




def add_product_to_wishlist(request):
    '''
    product add to wishlist database
    '''
    pid = request.GET['pid']
    user_id = UserInfo.objects.get(username = request.session['username'])
    if ProductWishlist.objects.filter(user_id_id = user_id.id).filter(product_id_id = pid).exists():
        return JsonResponse({'result':1})
    else:
        print('not in wishlist')
        add_product_to_wishlist = ProductWishlist()
        add_product_to_wishlist.user_id_id = user_id.id
        add_product_to_wishlist.product_id_id = pid
        add_product_to_wishlist.save()
        productwishllist = len(ProductWishlist.objects.filter(user_id_id = user_id.id).filter(user_id_id = user_id.pk))

    return JsonResponse({'result':0,"productwishllist":productwishllist})



def remove_wishlist(request):
    '''
    data remove from wishlist
    '''
    pid = request.GET['productid']
    user_id = UserInfo.objects.get(username = request.session['username'])
    ProductWishlist.objects.filter(user_id_id = user_id.id).filter(product_id_id = pid).delete()
    return JsonResponse({'value':True})

# wishlist end 





def addtocart_inwishlist(request):
    user_id = UserInfo.objects.get(username = request.session['username'])
    id = request.GET['id']
    if ProductCart.objects.filter(product_id_id = id).exists():
        return JsonResponse({'result':True})
    else:
        product_cart = ProductCart()
        product_cart.user_id_id = user_id.id
        product_cart.product_id_id = id
        product_cart.cart_quantity = 1
        product_cart.total_price = product_cart.product_id.is_offers
        product_cart.save()
        ProductWishlist.objects.get(product_id=id).delete()
        return JsonResponse({'result':False})