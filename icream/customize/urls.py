from django.urls import path
from . import views


urlpatterns = [
    
    path('user/',views.user_table,name='user_table'),
    path('product/',views.product_table,name='product_table'),
    path('user/block',views.user_block,name='user_block'),
    path('unblock/<id>/',views.user_unblock,name='user_unblock'),
    path('product/remove',views.delete_product,name='delete_product'),
    path('edituserdetails/<id>/',views.edit_product,name='edit_product'),
    path('category/',views.product_category,name='product_category'),
    path('addcategory/',views.add_product_category,name='add_product_category'),
    path('addproduct/',views.add_product,name='add_product'),
    path('banner/',views.banners,name='banners'),
    path('addbanner/',views.add_banner,name='add_banner'),
    path('salesreport/<order>/<amount>/<qty>/<list>/<category>',views.sales_report,name='sales_report'),
    
    
]
 