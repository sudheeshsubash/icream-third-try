from django.shortcuts import render,redirect
from home.models import Product,ProductCart,ProductWishlist,UserInfo
from payment.models import OrderAddField,OrderList,OrderCoupon,OrderPackage
from customize.models import Banner
from django.http import JsonResponse
from home.models import UserInfo
from logins import helper
from .forms import EditUserDetails
# Create your views here.


def guest_user_home(request):
    product_items = Product.objects.all()
    curosal = Banner.objects.all()
    if 'username' in request.session:
        user_id = UserInfo.objects.get(username = request.session['username'])
        cart_badge = len(ProductCart.objects.filter(user_id_id = user_id.id))
        wishlist_badge = len(ProductWishlist.objects.filter(user_id_id = user_id.id))
        return render(request,'guestUserHome.html',{'product_items':product_items,'curosal':curosal,'cart_badge':cart_badge,'wishlist_badge':wishlist_badge})
    return render(request,'guestUserHome.html',{'product_items':product_items,'curosal':curosal})



# about  

def about(request):
    if 'username' in request.session:
        user_id = UserInfo.objects.get(username = request.session['username'])
        cart_badge = len(ProductCart.objects.filter(user_id_id = user_id.id))
        wishlist_badge = len(ProductWishlist.objects.filter(user_id_id = user_id.id))
        return render(request,'about.html',{'cart_badge':cart_badge,'wishlist_badge':wishlist_badge})
    return render(request,'about.html',)





# user profile

def user_profile(request):
    user_info = UserInfo.objects.get(username = request.session['username'])
    orderpack_id = OrderPackage.objects.filter().order_by('-id')[:1]
    for x in orderpack_id:
        helper.orderpack_id = x.pk
    print(helper.orderpack_id)
    return render(request,'userprofile.html',{'user_info':user_info})   





# user order track

def user_order_track(request):
    user_id = UserInfo.objects.get(username = request.session['username'])
    order_history = OrderPackage.objects.filter(user_id = user_id.id)
    return render(request,'order.html',{'order_history':order_history})



def orders_all_product(request,id):
    order_history = OrderList.objects.filter(order_pack_id = id)
    return render(request,'orderproducts.html',{'order_history':order_history})

# cancel orders 

def cancel_order(request):
    print('this is ann error')
    order_id = request.GET['orderid']
    print(order_id)
    print(type(order_id))
    order_id = int(order_id)
    print(order_id,type(order_id))
    order_detail = OrderList.objects.get(id = order_id)
    order_detail.is_cancel = True
    order_detail.save()
    return JsonResponse({'yes':True})




def edituser_details(request,id):
    userinfo = UserInfo.objects.get(id=id)
    forms = EditUserDetails(request.POST or None,instance=userinfo)
    if request.method == 'POST':
        print('this is post method and edit user function is run')
        return redirect('user_profile')
    return render(request,'usereditdetails.html',{'forms':forms})







def addcoupon(request):
    '''
    this is apply coupon on total price
    '''
    coupon = request.GET['coupon']
    id  = helper.couponid = request.GET['id']
    print(f"coupon{coupon},coupon id {id}")
    ordercoupon = OrderCoupon.objects.get(id=id)
    ordercoupon.is_use = True
    ordercoupon.save()
    helper.coupontotal = helper.total * (100 - int(coupon))/100
    return JsonResponse({'total':helper.coupontotal})

