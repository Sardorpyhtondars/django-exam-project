from django.urls import path
from cart.views import cart_view, checkout_view, wishlist_view

app_name = 'cart'

urlpatterns = [
    path('wishlist/', wishlist_view, name='wishlist'),
    path('checkout/', checkout_view, name='checkout'),
    path('', cart_view, name='cart'),
]