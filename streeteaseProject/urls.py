from django.urls import path
from .views import product_list,product_detail,add_to_cart,cart_view,checkout_view,thank_you,menwomen,contact,home_view,aboutUs
urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout_view, name='checkout_view'),
    path('thank_you/', thank_you, name='thank_you'),
    path('home/', home_view, name='home_view'),
    path('contactUs/', contact, name='contactUs'),
    path('menWomen/', menwomen, name='menWomen'),
    path('aboutUs/', aboutUs, name='aboutUs'),


    # Add other paths as needed
]
