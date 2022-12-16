from django.shortcuts import render,redirect
import razorpay
from django.views.decorators.csrf import csrf_exempt
from home.forms import UserOrderPlace
from home.models import ProductCart,Orders,UserInfo,Product
from .models import OrderAddField,OrderAddress,OrderList,OrderCoupon,OrderPackage
from logins import helper
from .forms import AddAddress
from django.http import JsonResponse
from customize.models import Coupon
# Create your views here.



def save_to_database(request,id):
    user_id = UserInfo.objects.get(username = request.session['username'])
    cart_details = ProductCart.objects.filter(user_id_id = user_id.id)
    cart_length = len(cart_details)

    for x in range(cart_length):
        order = OrderList()
        order.user_id_id = user_id.id
        order.product_name = cart_details[x].product_id.product_name
        order.product_image = cart_details[x].product_id.product_image
        order.product_price = cart_details[x].product_id.product_price
        order.product_discription = cart_details[x].product_id.product_discription
        order.product_qty = cart_details[x].cart_quantity
        order.product_total = cart_details[x].total_price
        order.is_cancel = False
        order.is_delivered = False
        order.payment_type = helper.payment_type
        order.address_id = helper.address_id
        print(f"this is helper.id : {helper.address_id}")
        if helper.payment_type == 'cod':
            order.is_payment = False
        elif helper.payment_type == 'on':
            order.is_payment = True
        order.order_pack_id = helper.orderpack_id
        order.save()
        product_qty = Product.objects.get(id = cart_details[x].product_id.pk)
        product_qty.is_available = product_qty.is_available-cart_details[x].cart_quantity
        product_qty.save()
        cart_details[x].delete()



# online payment razopay

@csrf_exempt
def payment_with_razopay(request,total,id):
    print(total)
    if request.method == 'POST':
        client = razorpay.Client(auth=("rzp_test_4HjOMIihE6753m", "iQpYLgAzjV8fjB7UulrmXINv"))

        DATA = {
                "amount": 10000,
                "currency": "INR",
            }
        payment = client.order.create(data=DATA)
        
        return render(request,'paymentsuccess.html')

    save_to_database(request,id=id)
    return render(request,'paymentrazopay.html',{'total':total})




# cash on delivery

def cash_on_delivery(request,id,ptype):
    user_id = UserInfo.objects.get(username = request.session['username'])
    orderpack = OrderPackage()
    orderpack.user_id = user_id.pk
    if helper.couponid:
        orderpack.is_coupon_apply_id = helper.couponid
        orderpack.total_price = helper.coupontotal
    else:
        
        orderpack.total_price = helper.total
    
    orderpack.save()
    pack_id = OrderPackage.objects.filter().order_by('-id')[:1]
    for x in pack_id:
        helper.orderpack_id = x.id
    save_to_database(request,id=id)
    return render(request,'paymentsuccess.html')





# place order

def user_place_order(request):
    '''
    check order type is razorpay or cash on delivery 
    '''
    user_id = UserInfo.objects.get(username = request.session['username'])
    cart_details = ProductCart.objects.filter(user_id_id = user_id.id).select_related('product_id')
    previous_address = OrderAddress.objects.all()
    coupons_details = Coupon.objects.all()
    ordercoupon = OrderCoupon.objects.all()

    total = int()
    for c in cart_details:
        total += c.total_price

    helper.total = total
    
    if request.method == 'POST':
        previousaddress  = request.POST['previousaddress']
        paymenttype =  request.POST['paymenttype']

        helper.address_id = previousaddress
        helper.payment_type = paymenttype
        print(previousaddress)
        if paymenttype == 'cod':
            # return render(request,'cart.html')
            return redirect('cash_on_delivery',id=previousaddress,ptype=paymenttype)
        elif paymenttype == 'on':
            return redirect('payment_with_razopay',total=total,id=previousaddress)
    
    return render(request,'placeorder.html',{'cart_details':cart_details,'total':total,'previous_address':previous_address,"ordercoupon":ordercoupon})




# add new delivery address

def add_address(request):
    '''
    save new delivery address
    '''
    forms = AddAddress( request.POST or None )
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect('user_place_order')
    return render(request,'address.html',{'forms':forms})





























# def place_order(request):
#     '''
#     user order details and select payment method
#     '''

#     if len(ProductCart.objects.all()) < 1:
#         return redirect('cart')
#     user_id = UserInfo.objects.get(username = request.session['username'])
#     cart_details = ProductCart.objects.filter(user_id_id = user_id.id).select_related('product_id')
#     previous_address = OrderAddress.objects.all()
#     total = int()
#     for x in cart_details:
#         total += x.total_price

#     if request.method == 'POST':

#         try:
#             radio = helper.radio = request.POST['paymenttype']
#         except:
#             pass
#         else:
#             if radio == 'cod':
#                 if len(previous_address)>0:
#                     return redirect('payment_cash_on_delivery')
#                 return redirect('place_order')
#             elif radio == 'on':
#                 return redirect('payment_with_razopay')


#     return render(request,'placeorder.html',{'cart_details':cart_details,'total':total,'previous_address':previous_address})


# def online_payment_razorpay(request):
#     '''
#     razorpay
#     '''
#     pass


# def order_save_to_database(request):
#     '''
#     add to databse 
#     '''
#     user_id = UserInfo.objects.get(username = request.session['username'])
#     cart_details = ProductCart.objects.filter(user_id_id = user_id.id)
#     cart_length = len(cart_details)
#     for x in range(cart_length):
#         '''
#         the for loop concept is cart have more than 1 product so add each products
#         othervice database got an error
#         '''
        
#         order_obj = OrderAddField()
#         order_obj.username = request.session['username']
#         order_obj.product_name = cart_details[x].product_id.product_name
#         order_obj.product_image = cart_details[x].product_id.product_image
#         order_obj.product_price = cart_details[x].product_id.product_price
#         order_obj.product_discription = cart_details[x].product_id.product_discription
#         order_obj.order_type = helper.radio
#         order_obj.user_address = helper.address
#         order_obj.user_phone = helper.phone
#         order_obj.user_state = helper.state
#         order_obj.user_pincode = helper.pincode
#         order_obj.user_email = helper.email
#         order_obj.product_qty = cart_details[x].cart_quantity
#         order_obj.product_total = cart_details[x].total_price


# cod (cash on delivery)

# def payment_cash_on_delivery(request):
#     '''
#     order save to database is a fuction save details to database
#     '''
    
#     return render(request,'paymentsuccess.html')

