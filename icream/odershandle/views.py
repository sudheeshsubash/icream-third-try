from django.shortcuts import render,redirect
from payment.models import OrderList,OrderCoupon
from django.core.paginator import Paginator
from customize.models import Coupon
from customize.forms import AddCoupon
from django.http import JsonResponse
from home.models import Category,Product


# Create your views here.





def dashbord(request):
    if not 'adminusername' in request.session:
        '''
        session handle admin is not login canot show the page
        '''
        return redirect('guest_user_home')

    chart_data = OrderList.objects.all()
    category = Category.objects.all()
    total_order = len(chart_data)
    total_purchase_amount = int()
    total_product_qty = int()
    for data in chart_data:
        total_purchase_amount += data.product_price
        total_product_qty += data.product_qty

    barlist =[]

    for x in category:
        n=0
        for y in chart_data:
            p = Product.objects.get(product_name = y.product_name)
            if x.category_name == p.Cutegory_id.category_name:
                n+=1
        barlist.append(n)

    content = {
        'total_order':total_order,
        'total_purchase_amount':total_purchase_amount,
        'total_product_qty':total_product_qty,
        'barlist':barlist,
        'category':category,
    }

    return render(request,'dashbord.html',content)
    



def order_history(request):
    '''
    order history
    '''
    p = Paginator(OrderList.objects.all(),5)
    page = request.GET.get('page')
    order_details = p.get_page(page)
    return render(request,'orderhistory.html',{'order_details':order_details})




def coupon_view(request):
    '''
    coupon list
    '''
    _coupon_details = Coupon.objects.all()
    objects_pass={
        'coupon_details':_coupon_details
    }
    return render(request,'offers.html',objects_pass)




def add_coupons(request):
    '''
    add to coupon
    '''
    forms = AddCoupon(request.POST or None)
    objects_pass={
        'forms':forms
    }
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
            return redirect('coupon_view')
    return render(request,'addcouponcategory.html',objects_pass)





def cancle_coupon(request):
    '''
    id get current coupon id then delete that value in database
    '''
    id = request.GET['id']
    Coupon.objects.get(id = id).delete()
    return JsonResponse({'cancle':True})




def check_order_offers():
    print('this is offer price check functionality')
    offers = Coupon.objects.all()
    products = Product.objects.all()
    for off in offers:
        for product in products:
            if off.category == product.Cutegory_id:
                product.is_offers = product.product_price * (100 - off.offers)/100
                product.save()
                print(f"{off.category} - {product.Cutegory_id} :-: price = {product.product_price} offers - {off.offers} offerprice {product.is_offers}")




def coupons(request):
    coupons = OrderCoupon.objects.all()
    return render(request,'coupons.html',{'coupons':coupons})