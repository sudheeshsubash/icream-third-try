from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.product,name='product'),
    path('details<id>/',views.details,name='details'),
    path('cart/',views.cart,name='cart'),
    path('cart/i',views.increase_quantity_cart,name='increase_quantity_cart'),
    path('cart/d',views.decrese_quantity_cart,name='decrese_quantity_cart'),
    path('cart/remove',views.remove_cart,name='remove_cart'),
    path('product/addcart',views.add_to_cart,name='add_to_cart'),
    path('wishlist/',views.product_wishlist,name='product_wishlist'),
    path('product/addwishlist',views.add_product_to_wishlist,name='add_product_to_wishlist'),
    path('wishlist/remove/',views.remove_wishlist,name='remove_wishlist'),
    path('cproduct/<id>',views.category_product,name='category_product'),
    path('addtocartinwishlist/',views.addtocart_inwishlist,name='addtocart_inwishlist'),
    
    
]
