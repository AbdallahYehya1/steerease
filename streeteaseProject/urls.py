from django.urls import path
from .views import product_list,product_detail,add_to_cart,cart_view
urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/product/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),

    # Add other paths as needed
]
